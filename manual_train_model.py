import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# -----------------------
# Load Dataset
# -----------------------
df = pd.read_csv("dataset/student_performance_dataset.csv")

# -----------------------
# Select Only Important Columns
# -----------------------
df = df[[
    "age",
    "gender",
    "city_type",
    "study_hours_per_day",
    "attendance_percentage",
    "stress_level",
    "sleep_hours",
    "motivation_level",
    "ai_tool_usage_hours",
    "gaming_hours",
    "performance_category"
]]

# -----------------------
# Fill Missing Values
# -----------------------
df["sleep_hours"] = df["sleep_hours"].fillna(df["sleep_hours"].median())

# -----------------------
# Encode Text Columns
# -----------------------
encoders = {}

for col in ["gender", "city_type", "performance_category"]:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    encoders[col] = le

# -----------------------
# Features & Target
# -----------------------
X = df.drop("performance_category", axis=1)

y = df["performance_category"]

# -----------------------
# Train/Test Split
# -----------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------
# ANN Model
# -----------------------
model = MLPClassifier(
    hidden_layer_sizes=(32,16),
    max_iter=500,
    random_state=42
)

model.fit(X_train,y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test,prediction)

print()

print("="*40)

print("Manual Model Accuracy :",round(accuracy*100,2),"%")

print("="*40)

joblib.dump(model,"model/manual_model.pkl")

joblib.dump(encoders,"model/manual_encoders.pkl")

print()

print("Manual Model Saved Successfully")