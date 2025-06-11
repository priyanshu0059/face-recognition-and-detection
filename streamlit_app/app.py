# streamlit_app/app.py
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import cv2
import numpy as np
from app.config import Config
from app.logger import FaceLogger
from app.recognition import FaceRecognizer

# Initialize dependencies
face_cascade = cv2.CascadeClassifier(Config.CASCADE_PATH)
logger = FaceLogger()
recognizer = FaceRecognizer(known_faces_dir="known_faces")  # Adjust path as needed

# Streamlit UI
st.set_page_config(page_title="Face Recognition App", layout="wide")
st.title("🧠 Real-Time Face Recognition System")

start = st.button("Start Webcam")
stop = st.button("Stop")
frame_placeholder = st.empty()

if start:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, Config.FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Config.FRAME_HEIGHT)
    st.info("Running webcam... Press 'Stop' to exit.")

    run_flag = True

    while run_flag:
        ret, frame = cap.read()
        if not ret:
            st.warning("⚠️ Unable to read from webcam")
            break

        # Run face recognition
        results = recognizer.identify(frame)

        # Draw rectangles and names
        for (top, right, bottom, left), name in results:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Display frame
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(rgb_frame, channels="RGB")

        if stop:
            run_flag = False
            st.success("✅ Webcam stopped successfully")
            break

    if cap.isOpened():
        cap.release()
