import streamlit as st
import joblib
import numpy as np

# Load Model
model = joblib.load("regresion_model.joblib")

# Title
st.title("Student Placement Package Predictor")

st.write("Enter a CGPA to predict the expected package.")

# Input
cgpa = st.number_input(
    "Enter CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

# Prediction
if st.button("Predict Package"):

    input_data = np.array([[cgpa]])

    prediction = float(model.predict(input_data).flatten()[0])

    st.success(f"Predicted Package: {prediction:.2f} LPA")