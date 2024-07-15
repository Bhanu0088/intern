import cv2

# Open the camera
cap = cv2.VideoCapture(0)  # Use the appropriate camera index

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture a single frame
ret, frame = cap.read()
if not ret:
    print("Error: Could not read frame.")
    exit()

# Display the captured frame
cv2.imshow("Captured Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Release the camera
cap.release()
