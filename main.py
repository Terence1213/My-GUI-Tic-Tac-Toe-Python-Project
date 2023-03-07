from tkinter import *
import random

window = Tk()


def playTurn(row, column):

    if buttons[row][column]['text'] == "" and checkWinner() == False:

        buttons[row][column].config(text=player_turn.get())

        if checkWinner() == False:

            if player_turn.get() == "x":
                player_turn.set("o")

            else:
                player_turn.set("x")
            player_turn_label.config(text=f"{player_turn.get()}'s turn")

        elif checkWinner() == True:
            player_turn_label.config(text=f"{player_turn.get()} wins!")

        elif checkWinner() == "tie":
            player_turn_label.config(text="Tie!")

    """
    ------------------------------------------------------------------------------------------------------------
    AI FUNCTION OF THE TIC TAC TOE GAME - I plan to make a menu when starting the program, and then a new window
    pops up when the user chooses the play
    ------------------------------------------------------------------------------------------------------------ 
    if AIEnabled and player_turn.get() = "o":
        if buttons[row][column]['text'] == "" and checkWinner() == False:
        CURRENTLY WORKING ON HERE - IF THE SELECTED BOX IS ALREADY OCCUPIED, THIS PART OF THE PROGRAM LOOPS
            row = random.range(0, 3)
            column = random.range(0, 3)
            while buttons[row][column]['text'] != "":
                row = random.range(0, 3)
                column = random.range(0, 3)
            buttons[row][column].config(text=player_turn.get())
    """

def checkAllEmpty():
    result = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                result -= 1
    print(result)
    if result == 9:
        return True
    return False


def checkWinner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True

    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        return True

    if checkAllEmpty() == True:
        return "tie"

    return False


def startGame():
    players = ["x", "o"]
    player_turn.set(random.choice(players))
    player_turn_label.config(text=f"{player_turn.get()}'s turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""

player_turn = StringVar()
player_turn_label = Label(window, text="Player turn", font=("Arial", 30))
player_turn_label.pack()

game_table = Frame(window)

buttons = [[Button(game_table), Button(game_table), Button(game_table)],
           [Button(game_table), Button(game_table), Button(game_table)],
           [Button(game_table), Button(game_table), Button(game_table)]]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(game_table, font=("Arial", 50), height=1, width=3,
                                      command=lambda row=row, column=column: playTurn(row, column))
        buttons[row][column].grid(row=row, column=column)

restart_button = Button(window, text="Restart", font=("Arial", 15), command=startGame)
restart_button.pack()
game_table.pack()

startGame()
window.mainloop()
