import streamlit as st
import json
import requests

st.set_page_config(
    page_title="New User",
)

st.title("New User")

inputs = {
  "name": "hello",
  "email": "hello",
  "password": "hello"
}

if st.button('GO'):
    st.write(f'New user created')
    res = requests.post(url="http://127.0.0.1:8000/user/", data=json.dumps(inputs))
    st.subheader(f"Response from API: {res.text}")

if st.button('Show all'):
    res2 = requests.get(url="http://127.0.0.1:8000/user/")
    st.subheader(f"Response from API: {res2.text}")