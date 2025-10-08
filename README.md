# 🩺 Diabetes Prediction App

![Project Badge](https://img.shields.io/badge/Project-Diabetes%20Prediction-blue)
![Python Badge](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit Badge](https://img.shields.io/badge/Streamlit-1.0+-blue)
![License Badge](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

This project is a **Diabetes Prediction App** developed using Python, Machine Learning, and Streamlit. It allows users to input health-related parameters and predicts whether the individual is likely to have diabetes.

---

## ⚙️ Features

- **User-Friendly Interface**: Built with Streamlit for easy interaction.
- **Machine Learning Model**: Utilizes a trained Logistic Regression model.
- **Input Parameters**: Users can enter various health metrics.
- **Prediction Output**: Displays the likelihood of diabetes.

---

## 📊 Dataset

The model was trained on the **Pima Indians Diabetes Dataset**, which includes the following features:

- Pregnancies
- Glucose Level
- Blood Pressure (mm Hg)
- Skin Thickness (mm)
- Insulin Level
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

The target variable is whether the person has diabetes (`0` = No, `1` = Yes).

---

## 🛠️ Technologies Used

- Python 3.x  
- Streamlit: For creating the web application  
- Scikit-learn: For machine learning model  
- Pickle: For saving and loading the trained model  

---

## 🚀 Installation & Usage

pip install -r requirements.txt
streamlit run app.py

--> Enter the following health metrics:

1) Pregnancies

2) Glucose Level

3) Blood Pressure

4) Skin Thickness

5) Insulin Level

6) BMI

7) Diabetes Pedigree Function

8) Age

Click the "Predict" button.

The app will display whether the person is likely to have diabetes or not.

---


### 1. Clone the Repository

```bash
git clone https://github.com/RAJ-15012006/diabetes_prediction.git
cd diabetes_prediction

