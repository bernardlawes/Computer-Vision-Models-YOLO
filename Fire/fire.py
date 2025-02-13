from ultralytics import YOLO

path_to_input_image = '.\\_input\\fire.jpg'

path_to_pretrained_model =  '.\\Fire\\fire.pt'

model = YOLO(path_to_pretrained_model)
model.predict(source=path_to_input_image, imgsz=640, conf=0.6,save=True, project="_output")