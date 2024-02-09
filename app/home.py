import streamlit as st
import json
import requests
import pages

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("ML exchange")

option = st.selectbox("Choose between those 3 options :", ("Rock", "Paper", "Scissors"))

inputs = {"choice": option}

if st.button('Send request'):
    res = requests.post(url="http://127.0.0.1:8000/ml/predict", data= json.dumps(inputs))

    st.subheader(f"Response from AI : {res.json()['Prediction']}, so the result is : {res.json()['Result']} ! ")
