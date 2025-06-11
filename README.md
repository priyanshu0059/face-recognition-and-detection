# Face Recognition and Detection 🎯

This project is a Python-based application for real-time **face detection and recognition** using OpenCV and `face_recognition`. It leverages deep learning-based encodings to identify faces from a webcam or image feed.

---

## 🔍 Features

* ✅ Real-time **face detection** using OpenCV
* ✅ Accurate **face recognition** using pre-trained models
* ✅ Easy to add and encode new faces
* ✅ Works with both images and webcam video
* ✅ Simple and readable codebase

---

## 🛠️ Technologies Used

* Python 3.x
* OpenCV (`cv2`)
* `face_recognition` (built on `dlib`)
* NumPy
* OS, Pickle (for data handling)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/priyanshu0059/face-recognition-and-detection.git
cd face-recognition-and-detection
```

### 2. Install Dependencies

Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, manually install:

```bash
pip install opencv-python face_recognition numpy
```

---

## 📂 Project Structure

```
face-recognition-and-detection/
├── encodings/             # Stored face encodings
├── images/                # Known face images (training data)
├── dataset/               # Test dataset (optional)
├── main.py                # Main script for recognition
├── encode_faces.py        # Script to encode new faces
└── README.md              # Project documentation
```

---

## 📸 How to Use

### 1. Encode Known Faces

Place labeled images in the `images/` directory, then run:

```bash
python encode_faces.py
```

This script will encode faces and save them to the `encodings/` folder.

### 2. Run Face Recognition

```bash
python main.py
```

This will start your webcam and perform real-time face recognition.

---

## 🧠 How It Works

* The program detects faces using OpenCV’s `cv2` Haar cascades or deep learning models.
* It then compares the face encodings with known faces using the `face_recognition` library.
* If a match is found within the specified threshold, it identifies the person.

---

## ✅ To Do

* [ ] Add support for video file input
* [ ] Export recognition results to a log file
* [ ] Improve UI/UX with GUI (e.g., Tkinter or Streamlit)

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 🙌 Acknowledgements

* [face\_recognition](https://github.com/ageitgey/face_recognition) by @ageitgey
* OpenCV for powerful real-time image processing

---

If you'd like, I can also generate a `requirements.txt` file or help you publish a demo. Let me know!
