import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

def build_and_train_model(data, labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Model Evaluation:")
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    
    return model

def predict_and_evaluate(model, data, labels):
    y_pred = model.predict(data)

    print("Model predictions vs actual labels:")
    print(classification_report(labels, y_pred))
    print(f"Accuracy: {accuracy_score(labels, y_pred)}")
