from tkinter import * 

game = Tk()
game.geometry("400x400")

canvas = Canvas(game, width=400, height=400)
font1 = ("Book Antiqua", 20, "bold")
button1 = Button(game, text = "Start", font = font1)

player_move = 'x'

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
board = [row1,row2,row3]

def load_game():
    ok = 1

def opponent_move():
    global player_move
    player_move = 'o'

def user_move():
    global player_move
    player_move = 'x'

def opponent_play(): #generate opponent move
    ok = 1

def r1_c1():
    board[1][1] == player_move

def r1_c2():
    board[1][2] == player_move

def r1_c3():
    board[1][3] == player_move

def r2_c1():
    board[2][1] == player_move

def r2_c2():
    board[2][2] == player_move

def r3_c3():
    board[3][3] == player_move

def r3_c1():
    board[3][1] == player_move

def r3_c2():
    board[3][2] == player_move

def r3_c3():
    board[3][3] == player_move

game.mainloop()