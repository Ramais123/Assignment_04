import streamlit as st
import random

#initialize sessiom state for starting the random number

if 'random number' not in st.session_state:
    st.session_state['random number'] = random.randint(1, 10)

#initialize session state for number of attempts

if 'attempts' not in st.session_state:
    st.session_state['attempts'] = 0

#initialize session state for game over
st.set_page_config(page_title="Guess the Number", page_icon=" 😇",layout="centered")

#costum styling for the app
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff7e5f, #feb47b);
        padding: 20px;
        border-radius: 10px;
    }

    button[kind="secondary"] {
        background: linear-gradient(135deg, #ff7e5f, #feb47b) !important;
        color: black !important;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
        border: none;
    }

    button[kind="secondary"]:hover {
        background: linear-gradient(135deg, #feb47b, #ff7e5f) !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


#Game Header
st.markdown("<h1 style='text-align: center; color: #ff5733;'>☺️Guess the Number Game😌</h1>", unsafe_allow_html=True)
st.markdown("<h4 style= 'text-align: center; color: #333498db;'>I Have Choose a Number Between 1 and 10 ; Can you Guess this Number❓</h4>", unsafe_allow_html=True)
#Input for the user to guess the number
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

#check button

if st.button("Check"):
    st.session_state['attempts'] += 1
    if user_guess < st.session_state['random number']:
        st.warning("❌ Your guess is too low! Try again.😞")
    elif user_guess > st.session_state['random number']:
        st.warning("❌ Your guess is too high! Try again.😞")
    elif user_guess == st.session_state['random number']:
        st.success(f"🎉Congratulations! You guessed the Correct✅ number {st.session_state['random number']} in {st.session_state['attempts']} attempts!🎊")
        st.session_state['random number'] = random.randint(1, 10)  # Reset the random number for a new game
        st.session_state['attempts'] = 0  # Reset attempts for the new game
  
    else:
        st.error("Incorrect guess. PLease try again!")

#Reset button to start a new game
if st.button("®🔄Reset Game"):
    st.session_state['random number'] = random.randint(1, 10)  # Reset the random number
    st.session_state['attempts'] = 0  # Reset attempts for the new game
    st.rerun()