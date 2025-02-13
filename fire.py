from ultralytics import YOLO

path_to_input_image = '.\\data\\fire.jpg'

path_to_predictions = ".\\output\\"

path_to_model =  '.\\models\\fire.pt'

model = YOLO(path_to_model)
model.predict(source=path_to_input_image, imgsz=640, conf=0.6,save=True, project=path_to_predictions)
