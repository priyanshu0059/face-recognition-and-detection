# app/recognition.py
import os
import face_recognition
import numpy as np
import face_recognition.api as fr_api


class FaceRecognizer:
    def __init__(self, known_faces_dir="known_faces", tolerance=0.6):
        self.known_encodings = []
        self.known_names = []
        self.tolerance = tolerance

        if not os.path.exists(known_faces_dir):
            raise FileNotFoundError(f"[ERROR] Known faces directory '{known_faces_dir}' not found.")

        self._load_known_faces(known_faces_dir)

    def _load_known_faces(self, known_dir):
        for name in os.listdir(known_dir):
            person_dir = os.path.join(known_dir, name)
            if not os.path.isdir(person_dir):
                continue

            for img_name in os.listdir(person_dir):
                img_path = os.path.join(person_dir, img_name)
                try:
                    image = face_recognition.load_image_file(img_path)
                    encodings = face_recognition.face_encodings(image)
                    if encodings:
                        self.known_encodings.append(encodings[0])
                        self.known_names.append(name)
                        print(f"[INFO] Loaded face for '{name}' from '{img_name}'")
                    else:
                        print(f"[WARNING] No face found in image: {img_path}")
                except Exception as e:
                    print(f"[ERROR] Failed to process {img_path}: {e}")
def identify(self, frame):
    """
    Identify known faces in the given video frame.

    Args:
        frame (numpy.ndarray): The frame from webcam (BGR).

    Returns:
        List of tuples: [(top, right, bottom, left), name]
    """
    rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB

    try:
        locations = face_recognition.face_locations(rgb_frame)
        if not locations:
            return []

        encodings = face_recognition.face_encodings(rgb_frame, known_face_locations=locations)

        results = []

        for location, encoding in zip(locations, encodings):
            matches = face_recognition.compare_faces(self.known_encodings, encoding, self.tolerance)
            name = "Unknown"

            if True in matches:
                matched_index = matches.index(True)
                name = self.known_names[matched_index]

            results.append((location, name))

        return results

    except Exception as e:
        print(f"[ERROR] Face recognition failed: {e}")
        return []
