# Vision YOLO Models

A repository for YOLO-based computer vision models for object detection.

---

## Installation Guide

### 1️⃣ Clone the Repository**
Clone this repository to your local machine:

```sh
git clone https://github.com/YOUR_USERNAME/Vision-YOLO-Models.git
cd Vision-YOLO-Models
```

### 2️⃣ Set Up a Virtual Environment (Recommended)
Using a virtual environment helps isolate dependencies and avoid conflicts.

For Windows
```sh
python -m venv .venv
.venv\Scripts\activate
```

For MacOS / Linux
```sh
python -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Required Dependencies
Install all necessary packages from requirements.txt:
```sh
pip install -r requirements.txt
```

### 4️⃣ Verify Installation
Ensure all dependencies were installed correctly:
```sh
pip list
```

### 5️⃣ Running YOLO Model
To run the YOLO model on an image file:
```py
python vision.py input.jpg model.pt --show True
```
Running on a Video File
```py
python vision.py video.mp4 model.pt --show True
```
Running on a Live Camera
```py
python vision.py 0 --show True
```
### 5.5 Options
Running on Image and saving to disk
```py
python vision.py image.jpg --destination .\output\
```
Running on Image and showing to screen
```py
python vision.py image.jpg --show True
```
Running on Video, showing to screen, and Using GPU (By default, GPU use is True)
```py
python vision.py image.jpg --show True --gpu True
```

### 6️⃣ Updating Dependencies
If new dependencies are added, update requirements.txt:
```sh
pip freeze > requirements.txt
```

### 7️⃣ Contributing
We welcome contributions! Follow these steps:

Fork this repository 🍴
Create a new branch (git checkout -b feature-branch)
Make your changes and commit (git commit -m "Add new feature")
Push to your branch (git push origin feature-branch)
Open a Pull Request for review! ✅


### 8️⃣ License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

🔥 Happy Coding! 🚀
If you find this project useful, don’t forget to star ⭐ the repository!
