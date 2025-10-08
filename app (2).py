# app.py
import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go

# Load the saved Linear Regression model
with open("diabetes_linear_model (1).pkl", "rb") as f:
    model = pickle.load(f)

# Page config
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# Dark theme CSS
st.markdown("""
<style>
body {background-color: #0e1117; color: #ffffff; font-family: 'Segoe UI', sans-serif;}
.stButton>button {background-color: #4CAF50; color:white; font-size:18px; border-radius:10px; padding:10px 20px;}
.stNumberInput>div>div>input {background-color:#1e1e2f; color:white; border:1px solid #444; border-radius:5px; padding:5px;}
.stMarkdown h1 {color:#4CAF50; text-align:center;}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🩺 Diabetes Prediction App</h1>", unsafe_allow_html=True)
st.write("Enter patient details to predict diabetes risk:")

# Input columns
col1, col2 = st.columns(2)
with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, 0)
    glucose = st.number_input("Glucose Level", 0, 300, 120)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", 0, 200, 70)
    skin_thickness = st.number_input("Skin Thickness (mm)", 0, 100, 20)
with col2:
    insulin = st.number_input("Insulin Level", 0, 900, 79)
    bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    age = st.number_input("Age", 0, 120, 30)

# Predict button
# Predict button
if st.button("Predict Diabetes"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, diabetes_pedigree, age]])
    
    # Linear Regression prediction as risk score (scaled for demo)
    y_pred = model.predict(input_data)[0]
    probability = min(max(y_pred * 3, 0), 1)  # scale by 3 to push some predictions higher

    # Risk categories
    if probability < 0.3:
        risk_text = "Low Risk ✅"
        color = "green"
        emoji = "🟢"
    elif probability < 0.7:
        risk_text = "Medium Risk ⚠️"
        color = "yellow"
        emoji = "🟡"
    else:
        risk_text = "High Risk ⚠️"
        color = "red"
        emoji = "🔴"

    # Show text and progress bar
    st.markdown(f"<h3 style='color:{color};'>{emoji} {risk_text} ({probability*100:.2f}%)</h3>", unsafe_allow_html=True)
    st.progress(probability)

    # Detailed message
    if probability >= 0.5:
        st.error("⚠️ The patient is likely to have diabetes.")
    else:
        st.success("✅ The patient is unlikely to have diabetes.")

    # Gauge / donut chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability*100,
        number={'suffix': "%"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 30], 'color': "green"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}
            ]
        }
    ))
    st.plotly_chart(fig, use_container_width=True)
