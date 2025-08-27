import streamlit as st
import random

st.title("Rock Paper Scissors 🎮")

choices = ["rock", "paper", "scissors"]
player_choice = st.radio("Choose your move:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif ((player_choice == 'rock' and computer_choice == 'scissors') or
          (player_choice == 'scissors' and computer_choice == 'paper') or
          (player_choice == 'paper' and computer_choice == 'rock')):
        result = "You Win! 🎉"
    else:
        result = "You Lose! 😞"

    st.write(f"**Computer chose:** {computer_choice}")
    st.subheader(result)
