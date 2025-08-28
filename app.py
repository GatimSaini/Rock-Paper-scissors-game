import streamlit as st
import random

# Page setup
st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮", layout="centered")

# Custom CSS for beauty
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #e0f7fa, #fce4ec);
        padding: 2rem;
        border-radius: 15px;
    }
    .stButton button {
        background: #6200ea;
        color: white;
        border-radius: 12px;
        padding: 0.8em 1.2em;
        font-size: 1.1em;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: #3700b3;
        transform: scale(1.05);
    }
    .result-box {
        padding: 1rem;
        border-radius: 12px;
        font-size: 1.3em;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 style='text-align:center;'>✊ 🖐️ ✌️ Rock Paper Scissors</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Play against the computer and test your luck!</p>", unsafe_allow_html=True)

choices = {
    "🪨 Rock": "rock",
    "📄 Paper": "paper",
    "✂️ Scissors": "scissors"
}

col1, col2, col3 = st.columns(3)

player_choice = None
with col1:
    if st.button("🪨 Rock"):
        player_choice = "rock"
with col2:
    if st.button("📄 Paper"):
        player_choice = "paper"
with col3:
    if st.button("✂️ Scissors"):
        player_choice = "scissors"

if player_choice:
    computer_choice = random.choice(list(choices.values()))

    st.markdown(f"<h3 style='text-align:center;'>🤖 Computer chose: <b>{computer_choice.capitalize()}</b></h3>", unsafe_allow_html=True)

    if player_choice == computer_choice:
        result = "🤝 It's a Tie!"
        color = "#ff9800"
    elif ((player_choice == 'rock' and computer_choice == 'scissors') or
          (player_choice == 'scissors' and computer_choice == 'paper') or
          (player_choice == 'paper' and computer_choice == 'rock')):
        result = "🎉 You Win!"
        color = "#4caf50"
    else:
        result = "😞 You Lose!"
        color = "#f44336"

    st.markdown(
        f"<div class='result-box' style='background:{color}; color:white;'>{result}</div>",
        unsafe_allow_html=True
    )
