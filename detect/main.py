from log_generation import generate_player_logs
from cheat_detection import prepare_logs_for_training
from cheat_detection import apply_cheat_detection
from ml_model import build_and_train_model, predict_and_evaluate
from sklearn.metrics import classification_report, accuracy_score

from datetime import datetime
import random
import pandas as pd

def simulate_logs_and_train_model(num_players=10):
    start_time = datetime.now()
    num_ticks = int(900 / 0.05)  # 15 minutes of data

    # Simulate logs for multiple players
    for player_id in range(1, num_players + 1):
        is_cheater = random.random() < 0.1
        logs_df = generate_player_logs(start_time, num_ticks, is_cheater)
        logs_df.to_csv(f'read_next/player_{player_id}_logs.csv', index=False)

    # Prepare logs and train the model
    data, labels = prepare_logs_for_training('read_next')
    model = build_and_train_model(data, labels)
    
    return model

def run_prediction(model, num_players=10):
    # Simulate new logs for prediction
    start_time = datetime.now()
    num_ticks = int(900 / 0.05)
    logs = []

    for player_id in range(1, num_players + 1):
        is_cheater = random.random() < 0.1
        log_data = generate_player_logs(start_time, num_ticks, is_cheater)
        log_df = pd.DataFrame(log_data)

        # Apply cheat detection to get features (but NOT labels)
        log_df = apply_cheat_detection(log_df)
        logs.append(log_df)

    combined_logs = pd.concat(logs, ignore_index=True)

    # Make sure you are not trying to drop 'detected_label' (it won't exist here during prediction)
    X = combined_logs.drop(columns=['detected_label'], errors='ignore')  # Safely ignore if the column doesn't exist

    # There is no 'detected_label' during prediction, so we can't compare it directly
    y_true = combined_logs.get('detected_label')  # Use get to avoid KeyError if it doesn't exist

    # Predict using the model
    y_pred = model.predict(X)

    # If `y_true` exists, you can compare predictions
    if y_true is not None:
        print("Model predictions vs actual labels:")
        print(classification_report(y_true, y_pred))
        print(f'Accuracy: {accuracy_score(y_true, y_pred)}')
    else:
        print("Predictions made without actual labels (no comparison possible).")
        print(y_pred)


if __name__ == '__main__':
    # Step 1: Simulate logs and train the model
    trained_model = simulate_logs_and_train_model(num_players=10)
    
    # Step 2: Run predictions on new data
    run_prediction(trained_model, num_players=10)
