import random

#Add menu to choose between 2 player mode or single player mode
def start_game(mode):
    global players
    if mode == "single":
        players = ["Player1", "CPU"]
    else:
        players = ["Player1", "Player2"]
    new_game(buttons, label, players)
#Add a panel before the game board appears to choose between being Player1 or Player2
def choose_color():
    global player

    player = random.choice(players)

    label.config(text=player + " turn!")


#Implementation for a new game (2 players)
def new_game(buttons, label, players):
    global player

    player = random.choice(players)

    label.config(text=player+" turn!")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(
                text="",
                bg="#2e2e2e",
                fg="#ffffff" 
            )
    
# Implementation for a new game (You vs CPU)
def new_game_cpu(buttons, label, players):
    global player

    player = random.choice(players)

    label.config(text=player+" turn!")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(
                text="",
                bg="#2e2e2e",
                fg="#ffffff"
            )
# Function to check for a winner
def get_winner(buttons):
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                continue
            if buttons[row][column]['text'] == buttons[row][column + 1]['text'] == buttons[row][column + 2]['text']:
                return buttons[row][column]['text']
            if buttons[column][row]['text'] == buttons[column + 1][row]['text'] == buttons[column + 2][row]['text']:
                return buttons[column][row]['text']
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text']:
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text']:
        return buttons[0][2]['text']
    return False


