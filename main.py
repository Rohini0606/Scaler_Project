import pandas as pd
import streamlit as st
import pickle

st.header('Scaler Project - Insurance Premium Prediction')
df = pd.read_csv("/Users/rohin/PycharmProjects/Scaler_Project/renv/insurance.csv")
st.dataframe(df)

Diabetes = st.selectbox("Have Diabetes:", [1,0] )

BloodPressureProblems = st.selectbox( "Have BP:", [1,0] )
AnyTransplants = st.selectbox("Have AnyTransplants:", [1,0] )
AnyChronicDiseases = st.selectbox( "Have AnyChronicDiseases:", [1,0] )
KnownAllergies = st.selectbox( "Have KnownAllergies:", [1,0] )

HistoryOfCancerInFamily = st.selectbox( "Have HistoryOfCancerInFamily:", [1,0] )
NumberOfMajorSurgeries = st.selectbox( "Have NumberOfMajorSurgeries:", [0,1,2,3] )

Weight = st.slider("Set the Weight:", 50, 150, step = 10)
Height = st.slider("Set the Height:", 50, 190, step = 10)
Age = st.slider("Set the Age:", 18, 70, step = 1)

if st.button("Predict"):
    with open("Prediction", "rb") as file:
        reg_model = pickle.load(file)
        input_features = [
        [Age, Diabetes, BloodPressureProblems, AnyTransplants, AnyChronicDiseases, Height, Weight, KnownAllergies,
         HistoryOfCancerInFamily, NumberOfMajorSurgeries]]
    price = reg_model.predict(input_features)
    st.text("Predicted price is:"+str(price))
