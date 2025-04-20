import streamlit as st
import random

#Streamlit app title
st.title("🌟Fun Mad Libs Game")

#Sidebar for user input for blanks
st.sidebar.header("Fill in the Blanks😊")

#Taking user input
adj = st.sidebar.text_input("Enter an Adjective","Exciting") 
verb = st.sidebar.text_input("Enter a Verb","Explore")
verb1 = st.sidebar.text_input("Enter another Verb","Innovative")
famous_person = st.sidebar.text_input("Enter a Famous Person","Muhammad Ramais Khan")

#Fun Sentence
madlib_template = [
    f"Computer Programming is so{adj}! It makes me so exicted all the time because i have to{verb}. stay hydrated and {verb1} like your {famous_person}1",
    f"The world of AI is {adj}! every day , i wake up and {verb1} like {famous_person}., " 
    f"Success is {adj}. if you want to be like your {famous_person},you must {verb} every day and never forget to {verb1}!"
]

if st.button("Generate mad lib😎"):
    selected_madlib = random.choice(madlib_template)
    st.subheader("Here's Your Mad Lib!🤷‍♀️")
    st.write(selected_madlib)

    # footer
    st.write("Made with love❤️by Ramais Khan")

