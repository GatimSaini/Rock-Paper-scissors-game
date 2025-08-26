def play_game(player_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    result = ""
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif ((player_choice == 'rock' and computer_choice == 'scissors') or 
         (player_choice == 'scissors' and computer_choice == 'paper') or 
         (player_choice == 'paper' and computer_choice == 'rock')):
        result = "You Win! 🎉"
    else:
        result = "You Lose! 😞"
        
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.config(bg="#e0e0e0")

title_font = ('Helvetica', 16, 'bold')
button_font = ('Helvetica', 12)
result_font = ('Helvetica', 14, 'italic')

tk.Label(root, text="Choose your move!", font=title_font, bg="#e0e0e0").pack(pady=10)

button_frame = tk.Frame(root, bg="#e0e0e0")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock 🪨", font=button_font, command=lambda: play_game('rock'))
rock_button.pack(side="left", padx=10)

paper_button = tk.Button(button_frame, text="Paper 📄", font=button_font, command=lambda: play_game('paper'))
paper_button.pack(side="left", padx=10)

scissors_button = tk.Button(button_frame, text="Scissors ✂️", font=button_font, command=lambda: play_game('scissors'))
scissors_button.pack(side="left", padx=10)

result_label = tk.Label(root, text="", font=result_font, bg="#e0e0e0", height=4)
result_label.pack(pady=20)


root.mainloop()
