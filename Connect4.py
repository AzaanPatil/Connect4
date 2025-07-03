import random
from tkinter import Tk, Button, Label, Frame

def get_winner(buttons):
    # adapt to Connect4 rules
    # Check for vertical win
    for col in range(7):
        for row in range(3):
            if buttons[row][col]['text'] == buttons[row+1][col]['text'] == buttons[row+2][col]['text'] == buttons[row+3][col]['text'] != "":
                buttons[row][col].config(bg="green")
                buttons[row+1][col].config(bg="green")
                buttons[row+2][col].config(bg="green")
                buttons[row+3][col].config(bg="green")
                return True
    for row in range(6):
        for col in range(4):
           if buttons[row][col]['text'] == buttons[row][col+1]['text'] == buttons[row][col+2]['text'] == buttons[row][col+3]['text'] != "":
                buttons[row][col].config(bg="green")
                buttons[row][col+1].config(bg="green")
                buttons[row][col+2].config(bg="green")
                buttons[row][col+3].config(bg="green")
                return True
    for row in range(3):
        for col in range(7):
            if buttons[row][col]['text'] == buttons[row+1][col]['text'] == buttons[row+2][col]['text'] == buttons[row+3][col]['text'] != "":
                buttons[row][col].config(bg="green")
                buttons[row+1][col].config(bg="green")
                buttons[row+2][col].config(bg="green")
                buttons[row+3][col].config(bg="green")
                return True
    for row in range(3):
        for col in range(4):
            if buttons[row][col]['text'] == buttons[row+1][col+1]['text'] == buttons[row+2][col+2]['text'] == buttons[row+3][col+3]['text'] != "":
                buttons[row][col].config(bg="green")
                buttons[row+1][col+1].config(bg="green")
                buttons[row+2][col+2].config(bg="green")
                buttons[row+3][col+3].config(bg="green")
                return True
    for row in range(3, 6):
        for col in range(4):
            if buttons[row][col]['text'] == buttons[row-1][col+1]['text'] == buttons[row-2][col+2]['text'] == buttons[row-3][col+3]['text'] != "":
                buttons[row][col].config(bg="green")
                buttons[row-1][col+1].config(bg="green")
                buttons[row-2][col+2].config(bg="green")
                buttons[row-3][col+3].config(bg="green")
                return True
        
    # Check for horizontal win
    for row in range(6):
        for column in range(4):
            if buttons[row][column]['text'] == buttons[row][column+1]['text'] == buttons[row][column+2]['text'] == buttons[row][column+3]['text'] != "":
                buttons[row][column].config(bg="green")
                buttons[row][column+1].config(bg="green")
                buttons[row][column+2].config(bg="green")
                buttons[row][column+3].config(bg="green")
                return True
    # Check for vertical win
    for row in range(3):
        for column in range(7):
            if buttons[row][column]['text'] == buttons[row+1][column]['text'] == buttons[row+2][column]['text'] == buttons[row+3][column]['text'] != "":
                buttons[row][column].config(bg="green")
                buttons[row+1][column].config(bg="green")
                buttons[row+2][column].config(bg="green")
                buttons[row+3][column].config(bg="green")
                return True
    # Check for diagonal win (top-left to bottom-right)
    for row in range(3):
        for column in range(4):
            if buttons[row][column]['text'] == buttons[row+1][column+1]['text'] == buttons[row+2][column+2]['text'] == buttons[row+3][column+3]['text'] != "":
                buttons[row][column].config(bg="green")
                buttons[row+1][column+1].config(bg="green")
                buttons[row+2][column+2].config(bg="green")
                buttons[row+3][column+3].config(bg="green")
                return True
    # Check for diagonal win (bottom-left to top-right)
    for row in range(3, 6):
        for column in range(4):
            if buttons[row][column]['text'] == buttons[row-1][column+1]['text'] == buttons[row-2][column+2]['text'] == buttons[row-3][column+3]['text'] != "":
                buttons[row][column].config(bg="green")
                buttons[row-1][column+1].config(bg="green")
                buttons[row-2][column+2].config(bg="green")
                buttons[row-3][column+3].config(bg="green")
                return True
    # Check for tie
    if empty_spaces(buttons) is True:
        return False
    # If no winner and no empty spaces, it's a tie
    elif empty_spaces(buttons) is False:

        for row in range(6):
            for column in range(7):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    
    else:
        return False
def empty_spaces(buttons):
    spaces = 0
    for row in range(6):
        for column in range(7):
            if buttons[row][column]['text'] == "":
                spaces += 1
    if spaces == 0:
        return False
    else:
        return True

def empty_spaces(buttons):
    spaces = 0
    for row in range(6):
        for column in range(7):
            if buttons[row][column]['text'] == "":
                spaces += 1
    if spaces == 0:
        return False
    else:
        return True

