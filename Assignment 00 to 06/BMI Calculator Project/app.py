import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height in (cm)", 50, 250, 170)
weight = st.slider("Enter your weight in (kg)", 15, 200, 70)

bmi = weight / ((height / 100) ** 2)

st.write(f"Your BMI is: {bmi:.2f}")

st.write("### BMI Categories: ###")
st.write("Underweight: BMI Less than 18.5")
st.write("Normal weight: BMI Between 18.5 and 24.9")
st.write("Overweight: BMI Between 25 and 29.9")
st.write("Obesity: BMI 30 or greater")

