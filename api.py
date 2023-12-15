import streamlit as st
import joblib
import pandas as pd

st.title("Prediction of hospital admission")

st.write("##### This model helps in predicting the percentage of a patient's likelihood that he would be admitted into the hospital based on various factors and the hospital's amenities avilable")

st.sidebar.write("### Enter the inputs")
AGE = st.sidebar.number_input("Age (in number)",1.0,100.0)
HB= st.sidebar.number_input("Heamoglobin level (in g/DL)",5.0,25.0)
GLUCOSE= st.sidebar.number_input("Glucose (in mg/DL)",50.0,2700.0)

options = ['0', '1']
GENDER = st.radio("Gender (1 if male, 0 if female)", options)
RURAL = st.radio("Rural (1 if rural, 0 if urban)", options)
SMOKING = st.radio("Smoking (1 if smoker, 0 ifnon-smoker)", options)
ALCOHOL = st.radio("Alcohol (1 if you consume alcohol, 0 if non-alcoholic)", options)
DM = st.radio(" Diabetes Mellitus (1 if diabetic, 0 if non-diabetic)", options)
HTN = st.radio("Hypertension (1 if hypersion, 0 if non-hypertension)", options)
RAISED_CARDIAC_ENZYMES = st.radio(" Raise cardiac enzymes (1 if RCM Syomptomatic, 0 if non-RCM Symptomatic)", options)


submit = st.sidebar.button('Calculate')

if submit:
    model = joblib.load('model.pkl')
    input = [[AGE,GENDER, RURAL, SMOKING, ALCOHOL, DM, HTN, HB, GLUCOSE, RAISED_CARDIAC_ENZYMES]]
    Hospital = model.predict(input)
    st.write(" ## Percentage prediction : {:0.2f}".format(Hospital[0]))
else:
    st.write(" ## Percentage prediction :")
