import cv2
import numpy as np

# Function to format RGB values into a string
def get_color_name(b, g, r):
    return f"R={r}, G={g}, B={b}"

# Mouse event handler to display color under the cursor
def show_color_on_hover(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:  # Check if the mouse is moving
        # Get the RGB color at the current (x, y) position
        b, g, r = frame[y, x]
        color_text = get_color_name(b, g, r)
        
        # Copy the frame and overlay the color text
        display_frame = frame.copy()
        cv2.putText(display_frame, color_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('Live Color Detector', display_frame)

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# Create a window and set up a callback for mouse movements
cv2.namedWindow('Live Color Detector')
cv2.setMouseCallback('Live Color Detector', show_color_on_hover)

# Loop to continuously capture frames and display them
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the current video frame
    cv2.imshow('Live Color Detector', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the display window
cap.release()
cv2.destroyAllWindows()
