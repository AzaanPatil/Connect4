from tkinter import *
from Connect4 import get_winner
from Connect4UI import new_game
import random
import row


def next_turn(row, column): 
    global player 

    if buttons[row][column]['text'] == "" and get_winner(buttons) is False:

        if player == players[0]:
            buttons[row][column]["text"] = player
            if get_winner(buttons) is False:
                player = players[1]
                label.config(text=players[1] + " Turn") 
            elif get_winner(buttons) is True:
                label.config(text=players[0] + " Wins!")
            elif get_winner(buttons) == "Tie":
                label.config(text="Tie!")
        else:
            buttons[row][column]["text"] = player
            if get_winner(buttons) is False:
                player = players[0]
                label.config(text=players[0] + " Turn") 
            elif get_winner(buttons) is True:
                label.config(text=players[1] + " Wins!")
            elif get_winner(buttons) == "Tie":
                label.config(text="Tie")      


window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text= player + " turn", font=('consolas', 40))
label.pack(side="top")

reset = Button(
    text="restart",
    font=('consolas', 20),
    command=lambda: new_game(buttons, label, players)
)
reset.pack(side="top")

frame = Frame(window, bg="#2e2e2e")
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      bg="#2e2e2e", fg="#ffffff", activebg="#ffffff", activefg="#444444",
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column, padx=2, pady=2)

window.mainloop()

