import streamlit as st
import json
import requests

st.set_page_config(
    page_title="Login",
)

st.title("Login")

login = st.text_input('Enter your login')
password = st.text_input('Enter your password', type="password")

inputs = {"username": login, "password": password}

if login and password:
    if st.button('Sign In'):
        res = requests.post(url="http://127.0.0.1:8000/login", data=inputs)
        st.subheader(f"{login} is connected !")

        access_token = res.json()['access_token']
        token_type = res.json()['token_type']
