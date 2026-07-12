import pandas as pd

df = pd.read_csv("dataset/student_performance_dataset.csv")

cols = [
    "city_type",
    "mental_state",
    "internet_quality",
    "family_support",
    "financial_stress",
    "learning_style",
    "career_goal",
    "burnout_risk"
]

for c in cols:
    print("\n==============================")
    print(c)
    print("==============================")
    print(df[c].unique())