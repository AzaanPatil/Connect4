import random

def new_game(buttons, label, players):
    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(
                text="",
                bg="#2e2e2e",
                fg="#ffffff" 
            )
    

