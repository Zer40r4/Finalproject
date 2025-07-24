from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

def detect_objects_image(model_path, image_path, conf_threshold=0.3, save_results=True):
    model = YOLO(model_path)
    results = model(image_path, conf=conf_threshold)
    num_humans = 0
    num_hardHats  = 0

    for r in results:
        img = cv2.imread(image_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        boxes = r.boxes.xyxy.cpu().numpy()
        classes = r.boxes.cls.cpu().numpy()
        confidence = r.boxes.conf.cpu().numpy()

        for i, (box, cls, conf) in enumerate(zip(boxes, classes, confidence)):
            x1, y1, x2, y2 = box.astype(int)
            class_name = model.names[int(cls)]

            if class_name == "Humans":  # Change to "person" if needed
                num_humans += 1 
            if class_name == "Hard_hat":  # Change to actual name
                num_hardHats += 1
                
            cv2.rectangle(img_rgb, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{class_name}: {conf:.2f}"
            cv2.putText(img_rgb, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        if num_humans <= num_hardHats:
            print("Construction workers are currently safe!")
        else:
            print("Construction workers are unsafe. They are not wearing the proper PPEs.")

        plt.figure(figsize=(12, 8))
        plt.imshow(img_rgb)
        plt.axis('off')
        plt.title(f"YOLOv8 Detection - {len(boxes)} objects found")
        plt.show()

        if save_results:
            filename, ext = os.path.splitext(image_path)
            output_path = f"{filename}_detected{ext}"
            cv2.imwrite(output_path, cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
            print(f"\nAnnotated image saved as: {output_path}")

    return results

if __name__=="__main__":
    MODEL_PATH = "C:\\Users\\adebo\\Desktop\\Finalproject\\best.pt"
    print("1. Image detection")
    choice = input("Enter your choice: ")

    if choice == "1":
        IMAGE_PATH = input("Enter Image Path: ") 
        detect_objects_image(MODEL_PATH, IMAGE_PATH)

