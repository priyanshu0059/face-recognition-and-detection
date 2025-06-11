import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from app.config import Config
import os

class FaceAnalytics:
    def __init__(self):
        self.log_path = Config.LOG_FILE
        if not os.path.exists(self.log_path):
            raise FileNotFoundError("Log file not found. Run detection first.")

        self.df = pd.read_csv(self.log_path)
        self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])

    def plot_hourly_distribution(self, save_path="reports/charts/detections_per_hour.png"):
        self.df['Hour'] = self.df['Timestamp'].dt.hour
        hourly_data = self.df.groupby('Hour')['Face_Count'].sum()

        plt.figure(figsize=(10, 6))
        sns.barplot(x=hourly_data.index, y=hourly_data.values, palette="viridis")
        plt.title("Hourly Face Detections")
        plt.xlabel("Hour of the Day")
        plt.ylabel("Number of Detections")
        plt.xticks(range(0, 24))
        plt.tight_layout()

        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
        plt.show()
