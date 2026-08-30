# from ultralytics import YOLO
# from config import MODEL_PATH, DETECTION_THRESHOLD
# import cv2

# class DetectionService:
#     def __init__(self, model_path: str=MODEL_PATH):
#         self.model = YOLO(model_path)
#         self.class_names = {0: "no_Helmet", 1:"Helmet"}

#     def detect(self, frame):
#         results = self.model(frame)[0]

#         detections_classes = []
#         for result in results.boxes.data.tolist():
#             x1, y1, x2, y2 , score, class_id = result

#             if score >= DETECTION_THRESHOLD:
#                 class_name = self.class_names[int(class_id)]
#                 detections_classes.append(class_name)

#                 #Draw bounding box and label on the fram
#                 cv2.rectangle(frame, (int(x1), int(y1)),(int(x2), int(y2)), (0, 255, 0), 2)
#                 cv2.putText(frame, class_name, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)

#         return frame, detections_classes


import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import MODEL_PATH, DETECTION_THRESHOLD
from ultralytics import YOLO
import cv2


class DetectionService:

    def __init__(self, model_path: str = MODEL_PATH):
        # Load trained YOLO model
        self.model = YOLO(model_path)

        # Your trained model classes
        self.class_names = {0: "nohelmet",1: "helmet"}
        print("YOLO Model Classes:", self.model.names)

    def detect(self, frame):

        # Run YOLO detection
        results = self.model(frame, conf=DETECTION_THRESHOLD, verbose=False)[0]
        
        detections_classes = []

        # Check whether YOLO detected any boxes
        if results.boxes is None:
            return frame, detections_classes

        # Process every detection
        for detection in results.boxes.data.tolist():

            x1, y1, x2, y2, conf, cls_id = detection

            class_id = int(cls_id)

            # Ignore unknown classes
            if class_id not in self.class_names:
                continue

            class_name = self.class_names[class_id]

            detections_classes.append(class_name)

            # Convert coordinates to integers
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)

            # Label displayed on bounding box
            label = f"{class_name} {conf:.2f}"

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Draw class name and confidence
            cv2.putText(frame, label, (x1, max(y1 - 10, 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        return frame, detections_classes