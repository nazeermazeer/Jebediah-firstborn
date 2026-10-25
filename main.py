import time
import cv2

cap = cv2.VideoCapture(2)
if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()
    
time.sleep(1)
    
ret, frame = cap.read()
if not ret:
    print("Error: Could not read initial frame")
    exit()
    

bbox = cv2.selectROI("Select Object", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select Object")

x, y, w, h = map(int, bbox)

if w <= 0 or h <= 0:
    cap.release()
    cv2.destroyAllWindows()
    print(f"Invalid ROI {bbox}. Drag a rectangle around an object and confirm it.")
    exit()

tracker = cv2.TrackerKCF_create()
tracker.init(frame, (x, y, w, h))

try:
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to grab a frame.")
            break
                
        success, bbox = tracker.update(frame)

        x, y, w, h = map(int, bbox)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracker: KCF", (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow('Live Camera Feed', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q") or key == 27:
            break
except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()
