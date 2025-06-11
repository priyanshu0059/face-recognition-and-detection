import pandas as pd
from datetime import datetime
import os
from app.config import Config

class FaceLogger:
    def __init__(self):
        self.log_path = Config.LOG_FILE
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)

    def log_detection(self, face_count: int):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df = pd.DataFrame([[timestamp, face_count]], columns=["Timestamp", "Face_Count"])
        df.to_csv(self.log_path, mode='a', header=not os.path.exists(self.log_path), index=False)