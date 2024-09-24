import cv2
from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor


model = YOLO("yolov8n.pt")


results = model.predict(source="http://192.168.1.12:8080/video", show=True)  

for result in results:
    frame = result.orig_img  
    frame_resized = cv2.resize(frame, (640, 480)) 
    cv2.imshow("YOLO Stream", frame_resized)  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


