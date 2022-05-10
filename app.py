import streamlit as st
import joblib

model=joblib.load(open('spam_detect_model.pkl','rb'))
st.title("Email/SMS spam classifier")
input_sms=st.text_input("Enter the msg")
input_sms=[input_sms]

result=model.predict(input_sms)
if st.button('Predict'):
    if result==1:
        st.header("spam")
    else:
        st.header("not spam")
