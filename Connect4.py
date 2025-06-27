def get_winner(buttons):
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
           buttons[row][0].config(bg="green")
           buttons[row][1].config(bg="green")
           buttons[row][2].config(bg="green")
           return True
    
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
           buttons[0][column].config(bg="green")
           buttons[1][column].config(bg="green")
           buttons[2][column].config(bg="green")
           return True
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    elif empty_spaces(buttons) is False:
        
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="orange")   
        return "Tie"
    
    else:
        return False

def empty_spaces(buttons):
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

