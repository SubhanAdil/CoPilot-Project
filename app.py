import os
import io
import pandas as pd

from flask import (
    Flask,
    render_template,
    request,
    send_file
)

from predict import predict_student
from predict_csv import predict_dataset
from pdf_report import generate_pdf

app = Flask(__name__)

# ===============================
# Global Variables
# ===============================
latest_prediction_df = None
latest_dataset_df = None


# ===============================
# Home Page
# ===============================
@app.route("/")
def home():
    return render_template("index.html")


# ===============================
# Manual Prediction Page
# ===============================
@app.route("/manual")
def manual():
    return render_template("manual.html")


# ===============================
# Upload Page
# ===============================
@app.route("/upload")
def upload():
    return render_template("upload.html")


# ===============================
# Manual Prediction
# ===============================
@app.route("/predict", methods=["POST"])
def predict():

    data = {

        "age": int(request.form["age"]),
        "gender": request.form["gender"],
        "city_type": request.form["city_type"],
        "study_hours_per_day": float(request.form["study_hours_per_day"]),
        "attendance_percentage": float(request.form["attendance_percentage"]),
        "stress_level": int(request.form["stress_level"]),
        "sleep_hours": float(request.form["sleep_hours"]),
        "motivation_level": int(request.form["motivation_level"]),
        "ai_tool_usage_hours": float(request.form["ai_tool_usage_hours"]),
        "gaming_hours": float(request.form["gaming_hours"])

    }

    prediction, confidence = predict_student(data)

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence
    )


# ===============================
# Upload CSV
# ===============================
@app.route("/upload_csv", methods=["POST"])
def upload_csv():

    global latest_prediction_df
    global latest_dataset_df

    file = request.files["csv_file"]

    if file.filename == "":
        return "No File Selected"

    upload_folder = "uploads"

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    filepath = os.path.join(upload_folder, file.filename)

    file.save(filepath)

    # Read original dataset
    latest_dataset_df = pd.read_csv(filepath)

    # Prediction
    prediction_df = predict_dataset(filepath)

    latest_prediction_df = prediction_df.copy()

    # Dashboard Cards
    total = len(prediction_df)

    high = (prediction_df["Prediction"] == "High").sum()

    medium = (prediction_df["Prediction"] == "Medium").sum()

    low = (prediction_df["Prediction"] == "Low").sum()

    table = prediction_df.to_html(
        classes="table table-striped",
        index=False
    )

    # ===============================
    # Analytics
    # ===============================

    avg_study = round(latest_dataset_df["study_hours_per_day"].mean(),2)

    avg_sleep = round(latest_dataset_df["sleep_hours"].mean(),2)

    avg_attendance = round(latest_dataset_df["attendance_percentage"].mean(),2)

    avg_ai = round(latest_dataset_df["ai_tool_usage_hours"].mean(),2)

    avg_gaming = round(latest_dataset_df["gaming_hours"].mean(),2)

    avg_stress = round(latest_dataset_df["stress_level"].mean(),2)

    avg_exam = round(latest_dataset_df["final_exam_score"].mean(),2)

    highest_exam = latest_dataset_df["final_exam_score"].max()

    lowest_exam = latest_dataset_df["final_exam_score"].min()

    return render_template(

        "prediction_table.html",

        table=table,

        total=total,

        high=high,

        medium=medium,

        low=low,

        avg_study=avg_study,

        avg_sleep=avg_sleep,

        avg_attendance=avg_attendance,

        avg_ai=avg_ai,

        avg_gaming=avg_gaming,

        avg_stress=avg_stress,

        avg_exam=avg_exam,

        highest_exam=highest_exam,

        lowest_exam=lowest_exam

    )


# ===============================
# Download CSV
# ===============================
@app.route("/download_csv")
def download_csv():

    global latest_prediction_df

    if latest_prediction_df is None:
        return "No Prediction Found"

    output = io.StringIO()

    latest_prediction_df.to_csv(output,index=False)

    mem = io.BytesIO()

    mem.write(output.getvalue().encode())

    mem.seek(0)

    return send_file(

        mem,

        mimetype="text/csv",

        as_attachment=True,

        download_name="Predicted_Students.csv"

    )


# ===============================
# Download PDF
# ===============================
@app.route("/download_pdf")
def download_pdf():

    global latest_prediction_df

    if latest_prediction_df is None:
        return "No Prediction Found"

    if not os.path.exists("reports"):
        os.makedirs("reports")

    pdf_path = "reports/Student_Report.pdf"

    generate_pdf(pdf_path, latest_prediction_df)

    return send_file(

        pdf_path,

        as_attachment=True

    )


# ===============================
# Run
# ===============================
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)