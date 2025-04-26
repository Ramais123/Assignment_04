# File: app.py
import streamlit as st
import random
import string

st.set_page_config(page_title="Random Password Generator", page_icon="🔒", layout="centered")

st.title("🔐 Random Password Generator")
st.subheader("Secure, Fast, and Stylish Passwords")

st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .password-box {
        background: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    .password {
        font-size: 22px;
        font-weight: bold;
        color: #34495e;
        letter-spacing: 2px;
    }
</style>
""", unsafe_allow_html=True)

num_passwords = st.number_input("🔢 How many passwords?", min_value=1, max_value=20, value=5)
length_password = st.number_input("📏 Length of each password?", min_value=4, max_value=50, value=12)

if st.button("🚀 Generate Passwords"):
    st.subheader("🎯 Your Generated Passwords")
    for _ in range(num_passwords):
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length_password))
        st.markdown(f"<div class='password-box'><div class='password'>{password.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')}</div></div>", unsafe_allow_html=True)

st.markdown("""<hr style="margin-top: 50px;">""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; color: gray; font-size: 14px;">
    <h3>Made with ❤️ by <b>Muhamamd Ramais Khan</b> </h3>
</div>
""", unsafe_allow_html=True)
