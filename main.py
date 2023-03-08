from tkinter import *
import random

window = Tk()


def winCheck():

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


def playTurn(row, column):

    if buttons[row][column]['text'] == "" and checkWinner() == False:

        buttons[row][column].config(text=player_turn.get())

        winCheck()


def AITurn():

    if checkWinner() == False:

        while True:
            row = random.randrange(0, 3)
            column = random.randrange(0, 3)
            if buttons[row][column]['text'] == "":
                break

        buttons[row][column].config(text=player_turn.get())

        winCheck()

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

    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        buttons[2][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[0][2].config(bg="green")
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
            buttons[row][column].config(bg="white")


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

frame = Frame(window)
restart_button = Button(frame, text="Restart", font=("Arial", 15), command=startGame)
restart_button.grid(row=0, column=0)

AI_button = Button(frame, text="AI Turn", font=("Arial", 15), command=AITurn)
AI_button.grid(row=0, column=1)

frame.pack()
game_table.pack()

startGame()
window.mainloop()
