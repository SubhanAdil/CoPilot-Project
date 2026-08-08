# 🎓 EduAI Co-Pilot — Student Performance Analytics System

**EduAI Co-Pilot** is an AI-powered student performance analytics system developed to analyze student data, identify factors affecting academic outcomes, and generate data-driven insights using Machine Learning.

The project was developed as part of the **AI & Data Science training at Saylani Mass IT Training (SMIT)** and presented as a project for an **AI Innovation Hackathon**.

The system combines **Data Science, Machine Learning, and Flask** to provide an interactive platform for analyzing student performance and generating predictions.

---

## 🚀 Project Overview

Student performance can be influenced by many factors such as study habits, attendance, focus, stress, AI usage, sleep, and lifestyle patterns.

EduAI Co-Pilot uses student-related data to analyze these factors and predict student performance categories.

The system allows users to:

* Analyze student performance data
* Upload student data through CSV
* Generate ML-based predictions
* View prediction results and visualizations
* Identify patterns related to productivity and academic performance
* Generate downloadable PDF reports

---

## 📊 Dataset

The project uses a dataset containing:

* **3,000 student records**
* **32 features**

The features represent different aspects of student behavior and lifestyle, including:

* Study habits
* Attendance
* Focus score
* Stress level
* AI usage
* Sleep patterns
* Internet quality
* Family support
* Financial stress
* Learning style
* Mental state
* Other student-related factors

---

## 🧠 Machine Learning

The project follows a complete Machine Learning workflow:

1. Data collection
2. Data exploration
3. Data preprocessing
4. Missing value handling
5. Feature engineering
6. Categorical encoding
7. Model training
8. Model evaluation
9. Student performance prediction

The Machine Learning model was developed using **Scikit-learn**.

### Model Performance

**Accuracy: 86.17%**

The model is used to predict student performance based on the available student-related features.

---

## 🌐 Web Application

EduAI Co-Pilot was developed as a **Flask web application** to make the Machine Learning system interactive and easier to use.

### Main Features

#### 📁 CSV Upload

Users can upload student data in CSV format for batch prediction.

#### 👤 Manual Prediction

Users can enter student information manually and generate an individual prediction.

#### 📊 Data Visualization

Prediction results are presented through visualizations to make the results easier to understand.

#### 🤖 Machine Learning Prediction

The trained model processes the student data and generates performance predictions.

#### 📄 PDF Report Generation

The application can generate a downloadable PDF report containing prediction results and analysis.

#### 📥 CSV Results

Predicted student data can also be downloaded as a CSV file.

---

## 🛠️ Technologies Used

### Programming

* Python

### Data Science

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Machine Learning Classification
* Feature Engineering
* Categorical Encoding

### Web Development

* Flask
* HTML
* CSS
* JavaScript

### Tools

* Google Colab
* Jupyter Notebook
* GitHub

---

## 🔄 Project Workflow

```text
Student Data
     ↓
Data Preprocessing
     ↓
Missing Value Handling
     ↓
Feature Engineering
     ↓
Categorical Encoding
     ↓
Machine Learning Model
     ↓
Performance Prediction
     ↓
Flask Web Application
     ↓
Visualization & Reports
```

---

## 📁 Project Structure

```text
EduAI-Co-Pilot/
│
├── model/
│   ├── student_model.pkl
│   └── encoders.pkl
│
├── templates/
│   ├── index.html
│   ├── manual.html
│   └── prediction_table.html
│
├── reports/
│   └── Student_Report.pdf
│
├── app.py
├── predict_csv.py
├── requirements.txt
├── README.md
└── ...
```

> The exact files and folders may vary depending on the version of the project uploaded to this repository.

---

## 🎯 Key Outcomes

Through this project, I worked on a complete Data Science and Machine Learning workflow, including:

* Data cleaning and preprocessing
* Exploratory Data Analysis
* Feature engineering
* Categorical data encoding
* Machine Learning model training
* Model evaluation
* Prediction pipelines
* Flask application development
* Data visualization
* CSV processing
* Automated report generation

The project helped me apply Data Science and Machine Learning concepts to a practical education-focused problem.

---

## 🏆 Hackathon Project

**EduAI Co-Pilot** was developed in the context of an **AI Innovation Hackathon** focused on building AI Co-Pilots for real-world industry problems.

The hackathon's education analytics challenge focused on using student performance data to develop an AI-based solution.

---

## 👨‍💻 Author

**Syed Subhan Adil**

AI & Data Science | Machine Learning | Data Analytics

Developed during my **AI & Data Science training at Saylani Mass IT Training (SMIT), Karachi**.

---

## 📌 Future Improvements

Potential improvements for the project include:

* Improving model performance through additional experimentation
* Adding more advanced explainability features
* Adding authentication and user management
* Improving the dashboard and visualizations
* Deploying the application online
* Adding more student datasets for evaluation

---

## ⭐ Project

If you find this project useful or interesting, feel free to explore the repository and review the implementation.
