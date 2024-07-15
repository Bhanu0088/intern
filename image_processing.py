import numpy as np

# Background subtraction
fgbg = cv2.createBackgroundSubtractorMOG2()

# Read frames in a loop
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    fgmask = fgbg.apply(frame)
    
    # Display the result
    cv2.imshow('Foreground Mask', fgmask)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
