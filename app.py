import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("diabetes_model.pkl", "rb"))

st.title("Diabetes Risk Prediction")

st.write("Enter your health information:")

high_bp = st.selectbox("High Blood Pressure", [0, 1])
high_chol = st.selectbox("High Cholesterol", [0, 1])
chol_check = st.selectbox("Cholesterol Check", [0, 1])
bmi = st.slider("BMI", 10.0, 60.0, 25.0)
smoker = st.selectbox("Smoker", [0, 1])
phys_activity = st.selectbox("Physically Active", [0, 1])
fruits = st.selectbox("Eats Fruits Regularly", [0, 1])
veggies = st.selectbox("Eats Vegetables Regularly", [0, 1])
hvy_alcohol = st.selectbox("Heavy Alcohol Consumption", [0, 1])
any_healthcare = st.selectbox("Has Healthcare Access", [0, 1])
sex = st.selectbox("Sex", [0, 1])
age = st.slider("Age Group (1 to 13)", 1, 13, 5)

input_data = np.array([[high_bp, high_chol, chol_check, bmi, smoker, phys_activity, fruits,
                        veggies, hvy_alcohol, any_healthcare, sex, age]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction > 0.5:
        st.subheader(f"Prediction: High risk of diabetes ({prediction:.2f})")
    else:
        st.subheader(f"Prediction: Low risk of diabetes ({prediction:.2f})")
