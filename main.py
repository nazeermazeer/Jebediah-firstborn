import time
import cv2

class JebediahFirstborn:
    def __init__(self) -> None:
        self.video = cv2.VideoCapture(2)
        if not self.video.isOpened():
            raise RuntimeError("Could not open the webcam.")
            
        time.sleep(1)
            
        ret, frame = self.video.read()
        if not ret:
            raise RuntimeError("Could not read initial frame")
            

        bbox = cv2.selectROI("Select Object", frame, fromCenter=False, showCrosshair=True)
        cv2.destroyWindow("Select Object")

        x, y, w, h = map(int, bbox)

        if w <= 0 or h <= 0:
            self.video.release()
            cv2.destroyAllWindows()
            raise RuntimeError(f"Invalid ROI {bbox}. Drag a rectangle around an object and confirm it.")

        self.tracker = cv2.TrackerKCF_create()
        self.tracker.init(frame, (x, y, w, h))

    def trackObject(self) -> None:
        try:
            while True:
                ret, frame = self.video.read()
                
                if not ret:
                    raise RuntimeError("Failed to grab a frame.")
                        
                _, bbox = self.tracker.update(frame)

                x, y, w, h = map(int, bbox)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Tracker: KCF", (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame, f"({x}, {y})", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                cv2.imshow('Live Camera Feed', frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q") or key == 27:
                    break
        finally:
            self.video.release()
            cv2.destroyAllWindows()
            
            
if __name__ == "__main__":
    JebediahFirstborn().trackObject()
