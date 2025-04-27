import streamlit as st

st.title("Welcome to My Website")
st.header("Muhammad Ramais Khan")
st.subheader("GIAIC 2025")

name = st.text_input("Enter your name")
fname = st.text_input("Enter your father's name")
pnumber = st.text_input("Enter your phone number", max_chars=11, type="default") 
email = st.text_input("Enter your email")
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
class_name = st.selectbox("Select your class", ["1st", "2nd", "3rd", "4th", "5th"])
button = st.button("✅Done")
if button:
    st.markdown(f"""
                # Name: {name}
                # Father's Name: {fname}
                # Phone Number: {pnumber}
                # Email: {email}
                # Age: {age}
                # Class: {class_name}
                """ )
    




