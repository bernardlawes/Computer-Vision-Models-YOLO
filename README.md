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
To run the YOLO model on an image file and display to screen:
```sh
python .\scripts\<filename>.py input.jpg --show True
```
Running on an image file and saving to disk:
```sh
python .\scripts\<filename>.py input.jpg --save True
```
Running on a Video File
```sh
python .\scripts\<filename>.py video.mp4 --show True
```
Running on a Video File and saving to disk
```sh
python .\scripts\<filename>.py video.mp4 --ssave True
```
Running on a Live Camera
```sh
python .\scripts\<filename>.py 0 --show True
```
Running on a Live Camera and saving to disk
```sh
python .\scripts\<filename>.py 0 --ssave True
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
