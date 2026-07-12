import joblib
import pandas as pd

# Load model and encoders
model = joblib.load("model/manual_model.pkl")
encoders = joblib.load("model/manual_encoders.pkl")


def predict_student(data):

    df = pd.DataFrame([data])

    categorical = [
        "gender",
        "city_type"
    ]

    for col in categorical:
        df[col] = encoders[col].transform(df[col])

    prediction = model.predict(df)[0]

    confidence = max(model.predict_proba(df)[0]) * 100

    label = encoders["performance_category"].inverse_transform([prediction])[0]

    return label, round(confidence, 2)