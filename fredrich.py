import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

# Path to painting and face image
painting_path = "/Users/wim/Desktop/computer vision/friedrich_ii.jpg"
output_path = "/Users/wim/Desktop/computer vision/painting_with_blended_face.jpg"

# Load Friedrich's painting
painting_image = cv2.imread(painting_path)
if painting_image is None:
    print("Error: Could not load the painting.")
    exit()

# Resize the painting for consistency
painting_image = cv2.resize(painting_image, (800, 1000))

# Coordinates of Friedrich's face in the resized painting (adjusted upward)
px, py, pw, ph = 320, 140, 160, 200  # x, y (moved up by decreasing `py`), width, height of Friedrich's face

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam could not be accessed.")
    exit()

print("Press 's' to capture your face and blend it into Friedrich's painting.")
print("Press 'q' to quit.")

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not capture a frame from the webcam.")
        break

    # Convert the frame to grayscale for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    # Draw rectangles around detected faces (debugging)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Show webcam feed
    cv2.imshow("Webcam Feed - Press 's' to capture", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  # 's' to capture
        if len(faces) == 0:
            print("No faces detected. Please try again.")
            continue

        # Use the first detected face
        x, y, w, h = faces[0]
        detected_face = frame[y:y + h, x:x + w]

        # Resize the detected face to fit Friedrich's face region
        detected_face_resized = cv2.resize(detected_face, (pw, ph))

        # Convert to PIL for painterly effect
        face_pil = Image.fromarray(cv2.cvtColor(detected_face_resized, cv2.COLOR_BGR2RGB))
        face_pil = face_pil.filter(ImageFilter.SMOOTH_MORE)  # Smooth for a painted look
        face_pil = face_pil.filter(ImageFilter.DETAIL)  # Enhance edges
        face_pil = ImageEnhance.Color(face_pil).enhance(0.5)  # Reduce saturation
        face_pil = face_pil.filter(ImageFilter.GaussianBlur(radius=1))  # Slight blur for painting style

        # Convert back to OpenCV format
        detected_face_resized = cv2.cvtColor(np.array(face_pil), cv2.COLOR_RGB2BGR)

        # Create an alpha mask for fading
        mask = np.zeros((ph, pw), dtype=np.uint8)
        cv2.circle(mask, (pw // 2, ph // 2), min(pw, ph) // 2, 255, -1)  # Circular mask
        mask = cv2.GaussianBlur(mask, (51, 51), 0)  # Smooth edges

        # Extract Friedrich's face region
        painting_face = painting_image[py:py + ph, px:px + pw]

        # Blend the detected face with Friedrich's face using the alpha mask
        blended_face = cv2.seamlessClone(
            detected_face_resized, painting_face, mask, (pw // 2, ph // 2), cv2.NORMAL_CLONE
        )

        # Replace Friedrich's face region with the blended face
        painting_image[py:py + ph, px:px + pw] = blended_face

        # Save the final image
        cv2.imwrite(output_path, painting_image)
        print(f"Your blended painting has been saved to '{output_path}'.")

        # Display the result
        cv2.imshow("Blended Painting", painting_image)
        cv2.waitKey(3000)  # Show the result for 3 seconds
        break

    elif key == ord('q'):  # 'q' to quit
        print("Exiting the program.")
        break

# Release webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
