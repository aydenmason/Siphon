import numpy as np
import pandas as pd
import os

# Cheat detection logic
tick_interval = 0.05
max_sprint_jump_speed_with_potion = 9.976  # Speed with potion

def apply_cheat_detection(log_df):
    # Extract numeric time features from the timestamp
    log_df['hour'] = pd.to_datetime(log_df['timestamp']).dt.hour
    log_df['minute'] = pd.to_datetime(log_df['timestamp']).dt.minute
    log_df['second'] = pd.to_datetime(log_df['timestamp']).dt.second

    log_df['distance'] = np.sqrt((log_df['x2'] - log_df['x1'])**2 + (log_df['y2'] - log_df['y1'])**2 + (log_df['z2'] - log_df['z1'])**2)
    log_df['velocity'] = log_df['distance'] / tick_interval
    log_df['yaw_change'] = np.abs(log_df['yaw2'] - log_df['yaw1'])

    def detect_cheating(row):
        if row['velocity'] > max_sprint_jump_speed_with_potion:
            return 1
        elif row['yaw_change'] > 45:
            return 1
        elif row['y2'] - row['y1'] > 5:
            return 1
        return 0

    log_df['detected_label'] = log_df.apply(detect_cheating, axis=1)

    # Drop non-numeric columns (like the original timestamp and player name)
    log_df.drop(columns=['timestamp', 'player'], inplace=True)

    return log_df


def prepare_logs_for_training(folder='read_next'):
    data = []
    labels = []

    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            filepath = os.path.join(folder, filename)
            log_df = pd.read_csv(filepath)
            log_df = apply_cheat_detection(log_df)
            data.append(log_df.drop(columns=['detected_label']))
            labels.append(log_df['detected_label'])

    return pd.concat(data, ignore_index=True), pd.concat(labels, ignore_index=True)
