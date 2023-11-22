import streamlit as st
import joblib
import pandas as pd

st.title("Prediction of hospital admission")

st.write("##### This model helps in predicting the percentage of a patient's likelihood that he would be admitted into the hospital based on various factors and the hospital's amenities avilable")

st.sidebar.write("### Enter the inputs")
angle = st.sidebar.number_input("Hemoglobin (in g/dl)",1.0,359.9)
thickness = st.sidebar.number_input("Glucose (in mmol/L)",0.0,25.0)
vType = st.sidebar.number_input("Raised cardiac enzyme (in boolean)",1.0,200.0)
pRadius = st.sidebar.number_input("Heart disease (in boolean)",0.0,100.0)

submit = st.sidebar.button('Calculate')

if submit:
    model = joblib.load('HDHI Admission Data.csv')
    input = [[Hemoglobin, Glucose, Raised cardiac enzyme, Heart disease]]
    Hospital = model.predict(input)
    st.write(" ## Percentage prediction : {:0.2f}".format(Hospital[0]))
else:
    st.write(" ## Percentage prediction :")
