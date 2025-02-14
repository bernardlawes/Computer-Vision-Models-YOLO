from ultralytics import YOLO
import torch
import os, sys
import argparse
import cv2

# Create an argument parser
parser = argparse.ArgumentParser(description="Demo script for passing arguments.")

# Define expected arguments
parser.add_argument("source", type=str, help="Input File (an Image, Video File, or Camera ID)")
parser.add_argument("model", type=str, help="Pretrained Model File (.pt file)")
parser.add_argument("--destination", type=str, default="" , help="Preferred Output Path for Predictions")
parser.add_argument("--gpu", type=bool, default=True, help="Enable GPU Acceleration")
parser.add_argument("--show", type=bool, default=False, help="Enable verbose mode")

# Parse arguments
args = parser.parse_args()

# ---------------------------------------
# Set input on the input
# ---------------------------------------
source  = args.source.strip() if (args.source.strip().isdigit()) or (os.path.isfile(args.source.strip())) else ""
modelname = args.model.strip()
destination  = args.destination.strip() or ""

bool_gpu = args.gpu or False
bool_show = args.show or False

bool_stream = True if (source.isdigit()) or (os.path.splitext(source)[1] == ".mp4") else False
#bool_save = True if os.path.isdir(destination) else False
bool_save = True if len(destination) > 1 else False

if not os.path.isfile(source) and not source.isdigit():
    sys.exit("Error: Path to an Image, Video, or Camera ID is required")

def CameraFeed(id):
    # Open video stream (0 = default webcam)
    cap = cv2.VideoCapture(id)

    # Set the resolution lower if needed (reduces processing load)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    return cap

# Call the function
if source.isdigit(): CameraFeed(int(source))


print("\nSource: "+source,"\nmodel: "+modelname, "\noutdir: "+destination, "\ngpu: "+str(bool_gpu), "\nshow: "+str(bool_show), "\nstream: "+str(bool_stream), "\nsave : "+str(bool_save))


# ---------------------------------------
# Set process parameters
# ---------------------------------------

# ---------------------------------------
# Use GPU if it is available (you may need to change the CUDA_VISIBLE_DEVICES)
# ---------------------------------------
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
device = torch.device("cuda" if torch.cuda.is_available() and bool_gpu else "cpu")
print("Using device:", device)

# ---------------------------------------
# Load the model
# ---------------------------------------
model = YOLO(modelname)

# ---------------------------------------
# Run inference on the input
# ---------------------------------------

# non opencv method has this warning: WARNING ⚠️ inference results will accumulate in RAM unless `stream=True` is passed, causing potential out-of-memory
# errors for large sources or long-running streams and videos.
#model.predict(source=0, imgsz=640, conf=0.6, show=bool_show, stream=False, save=bool_save, device="cuda" if torch.cuda.is_available() else "cpu")
#exit()

for result in model.predict(source=source, stream=bool_stream, save=bool_save, device="cuda" if torch.cuda.is_available() else "cpu"):
    
    if bool_show:
        # Convert the result to an annotated frame
        frame = result.plot()

        # Display in OpenCV window
        cv2.imshow("YOLOv8 Real-Time Detection", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# ---------------------------------------
# Run inference on the input
# ---------------------
# ------------------
if bool_show:
    cv2.waitKey(0)
    cv2.destroyAllWindows()