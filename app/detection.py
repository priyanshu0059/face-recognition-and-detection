import cv2
from app.config import Config
from app.logger import FaceLogger

class FaceDetector:
    def __init__(self):
        self.logger = FaceLogger()
        self.face_cascade = cv2.CascadeClassifier(Config.CASCADE_PATH)

    def detect_faces_from_camera(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, Config.FRAME_WIDTH)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Config.FRAME_HEIGHT)

        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        print("[INFO] Starting real-time face detection. Press 'q' to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("[WARNING] Frame not read properly")
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=Config.DETECTION_SCALE_FACTOR,
                minNeighbors=Config.DETECTION_MIN_NEIGHBORS,
                minSize=Config.DETECTION_MIN_SIZE
            )

            face_count = len(faces)
            if face_count > 0:
                self.logger.log_detection(face_count)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Advanced Face Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()