import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

try:
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to grab a frame.")
            break

        cv2.imshow('Live Camera Feed', frame)
except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()
