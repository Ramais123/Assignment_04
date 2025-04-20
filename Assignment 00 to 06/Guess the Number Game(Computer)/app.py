import streamlit as st
import random

st.set_page_config(page_title="Computer Guesses!", page_icon="🧠", layout="centered")

if 'low' not in st.session_state:
    st.session_state.low = 1
if 'high' not in st.session_state:
    st.session_state.high = 10
if 'guess' not in st.session_state:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
if 'attempts' not in st.session_state:
    st.session_state.attempts = 1

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f6d365, #fda085);
        padding: 20px;
        border-radius: 10px;
        }
    h1, h3 {
        text-align: center;
        color: #5b0086;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🎮 Computer Will Guess Your Number!</h1>", unsafe_allow_html=True)
st.markdown(f"<h3>🤖 My Guess is: {st.session_state.guess}</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔼 Too High"):
        st.session_state.high = st.session_state.guess - 1
        st.session_state.attempts += 1
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        st.rerun()
with col2:
    if st.button("✅ Correct!"):
        st.success(f"🎉 I guessed your number in {st.session_state.attempts} attempts!")
with col3:
    if st.button("🔽 Too Low"):
        st.session_state.low = st.session_state.guess + 1
        st.session_state.attempts += 1
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        st.rerun()

if st.button("🔄 Reset Game"):
    for key in ['low', 'high', 'guess', 'attempts']:
        st.session_state.pop(key)
    st.rerun()
