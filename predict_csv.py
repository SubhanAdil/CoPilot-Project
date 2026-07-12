import joblib
import pandas as pd

# ==========================
# Load Model
# ==========================
model = joblib.load("model/student_model.pkl")
encoders = joblib.load("model/encoders.pkl")


# ==========================
# Predict Whole Dataset
# ==========================
def predict_dataset(filepath):

    # Read CSV
    df = pd.read_csv(filepath)

    # Save Student IDs
    student_ids = None

    if "student_id" in df.columns:
        student_ids = df["student_id"]

    # Remove target column
    if "performance_category" in df.columns:
        df = df.drop(columns=["performance_category"])

    # Remove Student ID
    if "student_id" in df.columns:
        df = df.drop(columns=["student_id"])

    # Encode categorical columns
    categorical = [
        "gender",
        "city_type",
        "mental_state",
        "learning_style",
        "career_goal"
    ]

    for col in categorical:
        if col in df.columns:
            df[col] = encoders[col].transform(df[col])

    # Fill Missing Values
    df = df.fillna(df.mean(numeric_only=True))

    # Make Prediction
    predictions = model.predict(df)

    # Convert numbers back to labels
    labels = encoders["performance_category"].inverse_transform(predictions)

    # Create Result DataFrame
    result = pd.DataFrame()

    if student_ids is not None:
        result["Student ID"] = student_ids

    result["Prediction"] = labels

    # Debug (optional)
    print(result.head())
    print(result.columns)

    return result