import streamlit as st
import random

#Game Title
st.markdown("""
     <style>
     body {
         background-color: #1e1e1e;
            color: white;
            font-family: 'Arial', sans-serif;  
            }
      .stButton>button {
            width: 100%;
            font-size: 10px;
            padding: 10px;
            border-radius: 10px;
            transition: 0.3s ease-in-out;
            }
        .stButton>button:hover {
            background-color: #ff4757 !important;
            color: white !important;
            }
            </style>
""", unsafe_allow_html=True)   

# Game Title
st.markdown("<h1 style='text-align: center; color:#ff4757 '>🗞️✂️Rock Paper Scissors</h1>", unsafe_allow_html=True)
# ("### 3 # for bold text")
st.write("### 🧑‍💻Play against the computer!")

#Game Logic

choices = ["rock 🤚", "paper 📜", "scissors s✂️"]
user_choice = st.selectbox("😎select your move:", choices)

if st.button("🔥Play Now!"):
    computer_choice = random.choice(choices)

    user_choice_clean = user_choice.split("[0]")  # Extract the emoji from the string
    computer_choice_clean = computer_choice.split("[0]")  # Extract the emoji from the string
    st.write(f"### 🤖 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        st.write("### It's a tie!")
    elif (user_choice == "rock 🤚" and computer_choice == "scissors s✂️") or \
         (user_choice == "paper 📜" and computer_choice == "rock 🤚") or \
         (user_choice == "scissors s✂️" and computer_choice == "paper 📜"):
        st.write("### You win! 🎉")
    else:
        st.write("### Computer wins! 😢")

    # Display Results
st.markdown(f"<h2 style='text-align: center; color: #ff4757;'>{st.write}</h2>", unsafe_allow_html=True)                
                
if st.button("🔄 Reset Game"):
    st.rerun()  # ✅ Corrected method to restart Streamlit app

    #footer
st.markdown("<h4 style='text-align: center; color: #ff4757;'>Made with 💖 by Ramais</h4>", unsafe_allow_html=True)
    

    