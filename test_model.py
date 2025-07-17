from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time
import nms_patch

def detect_objects_image(model_path, image_path, conf_threshold=0.5, save_results=True):
    model = YOLO(model_path)
    results = model(image_path, conf=conf_threshold)

    for r in results:
        img = cv2.imread(image_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        boxes = r.boxes.xyxy.cpu().numpy()
        classes = r.boxes.cls.cpu().numpy()
        confidence = r.boxes.conf.cpu().numpy()

        print(f"Found {len(boxes)} objects:")
        print("-" * 50)

        for i, (box, cls, conf) in enumerate(zip(boxes, classes, confidence)):
            x1, y1, x2, y2 = box.astype(int)
            class_name = model.names[int(cls)]

            print(f"Object {i+1}: {class_name} (confidence: {conf:.2f})")
            print(f"Bounding box: ({x1}, {y1}) to ({x2}, {y2})")

            cv2.rectangle(img_rgb, (x1, y1), (x2, y2), (0, 255, 0), 2)

            label = f"{class_name}: {conf:.2f}"
            cv2.putText(img_rgb, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        plt.figure(figsize=(12, 8))
        plt.imshow(img_rgb)
        plt.axis('off')
        plt.title(f"YOLOv8 Object Detection - {len(boxes)} objects found")
        plt.show()

        if save_results:
            output_path = image_path.replace('.', '_detected.')
            cv2.imwrite(output_path, cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
            print(f"\nAnnotated image saved as: {output_path}")

    return results

if __name__=="__main__":
    MODEL_PATH = "/home/nvidia/Finalproject/best.pt"

    print("Choose: ")
    print("1.image detection")
        
    choice = input("Enter your choice: 1")
    
    if choice == "1":
        IMAGE_PATH = input("Enter Image Path: ") 
        detect_objects_image(MODEL_PATH, IMAGE_PATH)   