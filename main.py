import tkinter as tk
import random
from PIL import Image, ImageTk
import os


def computer_move():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def play_game(player_choice):
    computer_choice = computer_move()
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=result)
    update_icons(player_choice, computer_choice)

def update_icons(player_choice, computer_choice):
    player_img_path = os.path.join('images', f'{player_choice}-user.png')
    computer_img_path = os.path.join('images', f'{computer_choice}.png')
    
    player_img = Image.open(player_img_path)
    computer_img = Image.open(computer_img_path)

    player_img = player_img.resize((150, 150), Image.ANTIALIAS)
    computer_img = computer_img.resize((150, 150), Image.ANTIALIAS)

    player_img = ImageTk.PhotoImage(player_img)
    computer_img = ImageTk.PhotoImage(computer_img)

    player_label.config(image=player_img)
    computer_label.config(image=computer_img)

    player_label.image = player_img
    computer_label.image = computer_img

root = tk.Tk()
root.title("Rock Paper Scissors")

#  player's choice, computer's choice
player_label = tk.Label(root)
player_label.grid(row=0, column=0, padx=10)

vs_label = tk.Label(root, text="VS", font=("Helvetica", 20))
vs_label.grid(row=0, column=1)

computer_label = tk.Label(root)
computer_label.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.grid(row=1, columnspan=3)

#  for player's choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_game('rock'))
rock_button.grid(row=2, column=0, pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game('paper'))
paper_button.grid(row=2, column=1, pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('scissors'))
scissors_button.grid(row=2, column=2, pady=10)


root.mainloop()
