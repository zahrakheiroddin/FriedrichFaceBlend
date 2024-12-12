import cv2
import sqlite3
from tkinter import simpledialog, Tk
import os
from datetime import datetime

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Oops! We couldn't access your webcam. Please make sure it's connected.")
    exit()

# Set up the SQLite database
conn = sqlite3.connect('face_database.db')
cursor = conn.cursor()

# Create a table to store detected faces if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Faces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    image_path TEXT
)
''')
conn.commit()

# Set up a hidden Tkinter root window to capture name input from the user
root = Tk()
root.withdraw()

# Show a message about how to interact with the program
print("Welcome to the Face Capture Program!")
print("Press 's' to capture a photo, or 'q' to quit.")

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame. Please try again.")
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Debugging message
    print(f"Currently, we've detected {len(faces)} face(s).")
    
    # Draw rectangles around faces in the frame
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the video feed with the detected faces
    cv2.imshow('Live Video - Press "s" to capture', frame)

    # Wait for the user to press a key
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  # 's' key to capture
        print("Photo captured successfully! Now, let’s name the person in the photo.")
        
        if len(faces) == 0:
            print("Sorry, no faces detected. Please try again.")
        else:
            # Ask for the person's name
            name = simpledialog.askstring("Face Detected", "Please enter the name of the person in the photo:", parent=root)
            if name:
                # Save the captured frame with face highlighted and name in the filename
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                image_path = f"captured_faces/{name}_{timestamp}.jpg"
                os.makedirs('captured_faces', exist_ok=True)
                cv2.imwrite(image_path, frame)
                print(f"Your photo has been saved as {image_path}.")

                # Store the name and image path in the database
                cursor.execute("INSERT INTO Faces (name, image_path) VALUES (?, ?)", (name, image_path))
                conn.commit()
                print(f"Thank you! '{name}' has been saved to the database.")

                # Optionally, display the captured image for 2 seconds as a confirmation
                cv2.imshow("Captured Image", frame)
                cv2.waitKey(2000)  # Show the image for 2 seconds
            else:
                print("No name entered. The image won't be saved.")

    elif key == ord('q'):  # 'q' key to quit
        print("Thank you for using the Face Capture Program. Goodbye!")
        break

# Release the webcam and close any open windows
cap.release()
cv2.destroyAllWindows()
conn.close()
