import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("dataset/student_performance_dataset.csv")

print("Dataset Shape:", df.shape)

# -----------------------------
# Remove student_id
# -----------------------------
if "student_id" in df.columns:
    df = df.drop("student_id", axis=1)

# -----------------------------
# Show Missing Values
# -----------------------------
print("\nMissing Values:\n")
print(df.isnull().sum())

# -----------------------------
# Fill Missing Values
# -----------------------------

# Numeric columns
numeric_cols = df.select_dtypes(include=["number"]).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Text columns
text_cols = df.select_dtypes(include=["object", "string"]).columns

for col in text_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# -----------------------------
# Encode Text Columns
# -----------------------------
encoders = {}

for col in text_cols:

    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(df[col])

    encoders[col] = encoder

# -----------------------------
# Features & Target
# -----------------------------
X = df.drop(["performance_category", "final_exam_score"], axis=1)

y = df["performance_category"]

# -----------------------------
# Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# ANN Model
# -----------------------------
model = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    max_iter=500,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("\n==============================")
print("Model Trained Successfully")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("==============================")

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "model/student_model.pkl")
joblib.dump(encoders, "model/encoders.pkl")

print("\nModel Saved Successfully")