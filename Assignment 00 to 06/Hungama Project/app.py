import streamlit as st
import random
import string

# --- Custom CSS Styling ---
custom_css = """
<style>
    .main {
        background-color: #fdfdfd;
    }
    h1 {
        color: #2E86AB;
        text-align: center;
        font-size: 3em;
    }
    .word-box {
        font-size: 2em;
        letter-spacing: 0.3em;
        text-align: center;
        color: #333;
        padding: 10px;
        border-radius: 10px;
        border: 2px dashed #2E86AB;
        background-color: #f0f8ff;
        margin-bottom: 20px;
    }
    .info-box {
        font-size: 1.2em;
        color: #444;
        margin-top: 10px;
    }
    .footer {
        margin-top: 40px;
        font-size: 0.9em;
        color: #aaa;
        text-align: center;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1>🪢 Hangman Game</h1>", unsafe_allow_html=True)

# --- Word list ---
word_list = ['python', 'streamlit', 'hangman', 'challenge', 'developer', 'keyboard']

# --- Game functions ---
def get_word():
    return random.choice(word_list).upper()

def display_word(word, guessed):
    return ' '.join([letter if letter in guessed else '_' for letter in word])

# --- Session State ---
if 'word' not in st.session_state:
    st.session_state.word = get_word()
    st.session_state.guessed = []
    st.session_state.tries = 6
    st.session_state.status = 'playing'

word = st.session_state.word
guessed = st.session_state.guessed
tries = st.session_state.tries
status = st.session_state.status

# --- Display Word Box ---
st.markdown(f'<div class="word-box">{display_word(word, guessed)}</div>', unsafe_allow_html=True)

# --- Display Info Boxes ---
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<div class='info-box'>🔤 <strong>Guessed Letters:</strong> {' '.join(guessed) if guessed else 'None'}</div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='info-box'>❤️ <strong>Tries Left:</strong> {tries}</div>", unsafe_allow_html=True)

# --- Game Input ---
if status == 'playing':
    letter = st.text_input("🔡 Guess a letter:", max_chars=1).upper()
    if st.button("✅ Submit Guess"):
        if letter and letter in string.ascii_uppercase:
            if letter in guessed:
                st.warning(f"⚠️ You've already guessed '{letter}'!")
            else:
                guessed.append(letter)
                if letter not in word:
                    st.session_state.tries -= 1
                if all([l in guessed for l in word]):
                    st.balloons()
                    st.success(f"🎉 You won! The word was '{word}'")
                    st.session_state.status = 'won'
                elif st.session_state.tries == 0:
                    st.error(f"💀 You lost! The word was '{word}'")
                    st.session_state.status = 'lost'
        else:
            st.error("❌ Please enter a valid letter (A-Z).")
else:
    st.info("ℹ️ Game over. You can restart below!")

# --- Restart Game ---
st.markdown("---")
if st.button("🔁 Restart Game"):
    st.session_state.word = get_word()
    st.session_state.guessed = []
    st.session_state.tries = 6
    st.session_state.status = 'playing'
    st.experimental_rerun()

# --- Footer ---
st.markdown("<div class='footer'> Made with 💖 By Muhammad Ramais Khan  </div>", unsafe_allow_html=True)
