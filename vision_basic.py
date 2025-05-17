from ultralytics import YOLO
import os

# ---------------------------------------
# Set input on the input
# ---------------------------------------
input_path   = '.\\data\\fire.png'  # Set path to video file
output_path  = ".\\output\\"        # Set path to output predictions

# ---------------------------------------
# Set process parameters
# ---------------------------------------
model_path   = '.\\model_fire.pt'         # Set path to model

# ---------------------------------------
# Load the model
# ---------------------------------------
model = YOLO(model_path)

# ---------------------------------------
# Run inference on the input
# ---------------------------------------
model = YOLO(model_path)
model.predict(source=input_path, imgsz=640, conf=0.6,save=True, project=output_path)
