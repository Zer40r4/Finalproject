import os
from roboflow import Roboflow
from ultralytics import YOLO
import nms_patch

from roboflow import Roboflow
rf = Roboflow(api_key="IWzJa3HicReV7dF7tNfU")
project = rf.workspace("zer40r4").project("final_project-nhtdz")
version = project.version(3)
dataset = version.download("yolov8")
                

# Initialize YOLO model
model = YOLO('yolov8n.pt')

# Train with AMP disabled and other Jetson-friendly settings
results = model.train(
    data=f"{dataset.location}/data.yaml",
    epochs=50,
    imgsz=640,
    batch=4, # Smaller batch for Jetson
    device=0,
    project="runs/train",
    name="roboflow_model",
    amp=False, # Disable AMP to avoid C++ ops issues
    verbose=True,
    patience=10,
    workers=2, # Reduce workers for Jetson
    cache=False, # Disable caching to save memory
    single_cls=False,
    rect=False,
    cos_lr=False,
    close_mosaic=10,
    resume=False,
    overlap_mask=True,
    mask_ratio=4,
    dropout=0.0,
    val=True,
    save=True,
    save_period=-1,
    plots=True,
    deterministic=True,
    seed=0,
    exist_ok=False,
    pretrained=True,
    optimizer='AdamW',
    lr0=0.01,
    lrf=0.1,
    momentum=0.937,
    weight_decay=0.0005,
    warmup_epochs=3.0,
    warmup_momentum=0.8,
    warmup_bias_lr=0.1,
    box=7.5,
    cls=0.5,
    dfl=1.5,
    pose=12.0,
    kobj=1.0,
    label_smoothing=0.0,
    nbs=64,
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,
    degrees=0.0,
    translate=0.1,
    scale=0.5,
    shear=0.0,
    perspective=0.0,
    flipud=0.0,
    fliplr=0.5,
    mosaic=1.0,
    mixup=0.0,
    copy_paste=0.0
)

print("Training completed!")
print(f"Model saved to: runs/train/roboflow_model/weights/best.pt")

# Test the trained model
model = YOLO('runs/train/roboflow_model/weights/best.pt')
results = model.val() # Validate
print(f"mAP50: {results.box.map50}")
print(f"mAP50-95: {results.box.map}")

