# run.py
from app.detection import FaceDetector
import sys


def main():
    try:
        print("[INFO] Initializing face detector...")
        detector = FaceDetector()
        detector.detect_faces_from_camera()
    except KeyboardInterrupt:
        print("[INFO] Interrupted by user. Exiting..."),
        sys.exit(0)
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()