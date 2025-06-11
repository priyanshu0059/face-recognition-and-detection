import os
import cv2

# Configuration for paths and detection parameters
class Config:
    CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    LOG_FILE = os.path.join("data", "face_log.csv")
    FRAME_WIDTH = 640
    FRAME_HEIGHT = 480
    DETECTION_SCALE_FACTOR = 1.1
    DETECTION_MIN_NEIGHBORS = 5
    DETECTION_MIN_SIZE = (30, 30)