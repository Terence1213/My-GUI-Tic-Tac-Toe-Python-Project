from tkinter import *
import random
window = Tk()

table = [{"A1" : "-", "A2" : "-", "A3" : "-"},
         {"B1" : "-", "B2" : "-", "B3" : "-"},
         {"C1" : "-", "C2" : "-", "C3" : "-"},]



def restartGame():
    pass

def checkWinner():
    pass

#CURRENTLY DOING: MAKING IT SO WHEN THE USER PLAYS, THE PLAY IS DISPLAYED ON THE BUTTON.
def playTurn(player_choice):
    global table
    for row in table:
        if row.get(player_choice) == "-":
            row[player_choice] = player_turn.get()
            if player_turn.get() == "x":
                player_turn.set("o")
            else:
                player_turn.set("x")
    player.config(text=player_turn.get())


def startGame():
    players = ["x", "o"]
    player_turn.set(random.choice(players))
    player.config(text=player_turn.get())

player_turn = StringVar()

game_table = Frame(window)
A1_button = Button(game_table, font=("Arial", 50), height=1, width=3, command=lambda: playTurn("A1")).grid(row=0, column=0)
A2_button = Button(game_table, font=("Arial", 50), height=1, width=3, command=lambda: playTurn("A2")).grid(row=0, column=1)
A3_button = Button(game_table, font=("Arial", 50), height=1, width=3, command=lambda: playTurn("A3")).grid(row=0, column=2)
B1_button = Button(game_table, font=("Arial", 50), height=1, width=3, command=lambda: playTurn("B1")).grid(row=1, column=0)
B2_button = Button(game_table, font=("Arial", 50), height=1, width=3, command=lambda: playTurn("B2")).grid(row=1, column=1)
B3_button = Button(game_table, font=("Arial", 50), height=1, width=3, command=lambda: playTurn("B3")).grid(row=1, column=2)
C1_button = Button(game_table, font=("Arial", 50), height=1, width=3, command=lambda: playTurn("C1")).grid(row=2, column=0)
C2_button = Button(game_table, font=("Arial", 50), height=1, width=3, command=lambda: playTurn("C2")).grid(row=2, column=1)
C3_button = Button(game_table, font=("Arial", 50), height=1, width=3, command=lambda: playTurn("C3")).grid(row=2, column=2)
player = Label(window, text="Player turn", font=("Arial", 30))
restart_button = Button(window, text="Restart", command=restartGame)
player.pack()
game_table.pack()

startGame()
window.mainloop()

