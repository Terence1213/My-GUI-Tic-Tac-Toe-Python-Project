from tkinter import *
import random

window = Tk()

#Checks if the player who just played his turn won.
def winCheck():

    #If no one has won the game yet, the player turn is switched to the other player.
    if checkWinner() == False:

        #Therefore if the player turn was "x", it is now set to "o"
        if player_turn.get() == "x":
            player_turn.set("o")

        #And if the player turn was "o", it is now set to "x"
        else:
            player_turn.set("x")

        #Then, the player turn label, which shows the present player turn is updated.
        player_turn_label.config(text=f"{player_turn.get()}'s turn")

    #The player who won is displayed if a player wins.
    elif checkWinner() == True:
        player_turn_label.config(text=f"{player_turn.get()} wins!")

    #Tie is displayed if the method checkWinner() returns "tie"
    elif checkWinner() == "tie":
        player_turn_label.config(text="Tie!")


#The actual player's turn.
def playTurn(row, column):

    #If the button / box the player enters in the table is blank, and the game is still not won / over,
    #his play is marked on the table, and the program checks if he has won the game.
    if buttons[row][column]['text'] == "" and checkWinner() == False:

        buttons[row][column].config(text=player_turn.get())

        winCheck()


#The program plays a random unplayed spot in the table
def AITurn():

    #If the game hasn't been won yet...
    if checkWinner() == False:

        #The program makes a different combinations of rows and columns until it finds a coordinate which hasn't already
        #been filled yet.
        while True:
            row = random.randrange(0, 3)
            column = random.randrange(0, 3)
            if buttons[row][column]['text'] == "":
                break

        #Then, the selected box's text is configured depending on the player turn (either "x", or "o").
        buttons[row][column].config(text=player_turn.get())

        #Again, the program checks if this player has won the game.
        winCheck()


def checkAllFull():
    result = 9

    #For each box in the table, the program checks if the value of the text in the table is blank.
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                #If the text in the box is empty, the result is subtracted by 1
                result -= 1

    #If the result were to be not 9, (a smaller value), that would mean that at least one of the boxes are empty
    #(since at some point, the variable "result" was subtracted by 1), and so not all boxes are full / played,
    #so the program returns false.
    if result == 9:
        return True
    return False


#Checks if the player who just played has won the game.
def checkWinner():

    #Checks for row wins.
    for row in range(3):
        #For each row, the program checks if box 1 matches with box 2 and box 3, and that none of them are blank.
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            #If true, then the game is won, and the matching boxes are configured to a background color of green.
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        #For each column, the program checks if box 1 matches with box 2 and box 3, and that none of them are blank.
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            #If true, then the game is won, and the matching boxes are configured to a background color of green.
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    #Checks for top left to bottom right diagonal win.
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        #If true, then the game is won, and the matching boxes are configured to a background color of green.
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    #Checks for bottom left to top right diagonal win.
    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        #If true, then the game is won, and the matching boxes are configured to a background color of green.
        buttons[2][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[0][2].config(bg="green")
        return True

    #If no one has won yet, but all the boxes are full (played), then the game is a tie.
    if checkAllFull() == True:
        return "tie"

    #If no one has won yet, and not all boxes have been filled, than the game is still not over.
    return False


def startGame():
    #The starting player is being chosen randomly, and then the label is being configured accordingly to that player.
    players = ["x", "o"]
    player_turn.set(random.choice(players))
    player_turn_label.config(text=f"{player_turn.get()}'s turn")

    #All the boxes are being reset to blank and white.
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""
            buttons[row][column].config(bg="white")

#The player turn, which is used all throughout the program.
player_turn = StringVar()

#The label which displays the present player turn. (and also shows if anyone has won the game, or if the game is a tie).
player_turn_label = Label(window, font=("Arial", 30))
player_turn_label.pack()

#The frame which contains all the boxes
game_table = Frame(window)

#The boxes / buttons being initialised for error reasons.
buttons = [[Button(game_table), Button(game_table), Button(game_table)],
           [Button(game_table), Button(game_table), Button(game_table)],
           [Button(game_table), Button(game_table), Button(game_table)]]

#The boxes / buttons being actually initialised, and made functional.
for row in range(3):
    for column in range(3):
        #For each coordinate in the table, the button is created to accordingly make a play with only 1 method -
        #"playturn()"
        buttons[row][column] = Button(game_table, font=("Arial", 50), height=1, width=3,
                                      command=lambda row=row, column=column: playTurn(row, column))
        buttons[row][column].grid(row=row, column=column)

#The frame which contains the restart button and the AI button
frame = Frame(window)

#The game restarts
restart_button = Button(frame, text="Restart", font=("Arial", 15), command=startGame)
restart_button.grid(row=0, column=0)

#Makes a random play (AI play)
AI_button = Button(frame, text="AI Turn", font=("Arial", 15), command=AITurn)
AI_button.grid(row=0, column=1)

#The frame and table are displayed on the window.
frame.pack()
game_table.pack()

#The game is started
startGame()

#The window is prompted / displayed to the user.
window.mainloop()
