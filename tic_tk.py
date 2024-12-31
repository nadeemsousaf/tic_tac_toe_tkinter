from tkinter import *
import random

game = Tk()
game.geometry("400x400")

canvas = Canvas(game, width=400, height=400)

font1 = ("Arial", 40, "bold")
font2 = ("Arial", 20, "bold")

empty = "    "
user = " X "
opponent = " O "

board = []
taken_positions = 0

class square:
    def __init__(self, button, x_num, y_num, type):
        self.button = button
        self.x_num = x_num
        self.y_num = y_num
        self.type = type
        
def create_board():
    board.append(square(button_r1_c1,600,250,empty))
    board.append(square(button_r1_c2,800,250,empty))
    board.append(square(button_r1_c3,1000,250,empty))
    board.append(square(button_r2_c1,600,450,empty))
    board.append(square(button_r2_c2,800,450,empty))
    board.append(square(button_r2_c3,1000,450,empty))
    board.append(square(button_r3_c1,600,650,empty))
    board.append(square(button_r3_c2,800,650,empty))
    board.append(square(button_r3_c3,1000,650,empty))

def new_move():
    global player
    if player == user:
        player = opponent
        opponent_play()
    else:
        player = user

def opponent_play(): #generate opponent move
    found_move = False
    while found_move == False and taken_positions < 9:
        position = random.randrange(0,8)
        if board[position].type == empty:
            found_move = True #we have found a valid move
            if position == 0:
                r1_c1()
            elif position == 1:
                r1_c2()
            elif position == 2:
                r1_c3()
            elif position == 3:
                r2_c1()
            elif position == 4:
                r2_c2()
            elif position == 5:
                r2_c3()
            elif position == 6:
                r3_c1()
            elif position == 7:
                r3_c2()
            else:
                r3_c3()

def start():
    create_board()
    load_board()

def load_board():
    canvas.pack(fill="both", expand=True)
    for i in board:
        canvas.create_window(i.x_num, i.y_num, window = i.button)
    canvas.create_window(1425, 55, window = button_quit)
    canvas.create_window(130, 55, window = button_restart) #here

def formal_end_game(message):
    canvas.create_text(800, 100, text = message, font=font2)
    disable_squares()

def disable_squares():
    button_r1_c1.configure(state="disabled")
    button_r1_c2.configure(state="disabled")
    button_r1_c3.configure(state="disabled")
    button_r2_c1.configure(state="disabled")
    button_r2_c2.configure(state="disabled")
    button_r2_c3.configure(state="disabled")
    button_r3_c1.configure(state="disabled")
    button_r3_c2.configure(state="disabled")
    button_r3_c3.configure(state="disabled")

def enable_squares(): #here
    button_r1_c1.configure(state="normal")
    button_r1_c2.configure(state="normal")
    button_r1_c3.configure(state="normal")
    button_r2_c1.configure(state="normal")
    button_r2_c2.configure(state="normal")
    button_r2_c3.configure(state="normal")
    button_r3_c1.configure(state="normal")
    button_r3_c2.configure(state="normal")
    button_r3_c3.configure(state="normal")

def reset_globals(): #here
    global board, taken_positions, player
    board = []
    taken_positions = 0
    player = user

def reset_board(): #here
    enable_squares()
    reset_globals()
    start()

def valid_move(button, position):
    global taken_positions
    button.configure(text=player)
    board[position].type = player
    taken_positions += 1
    check_game_status()
    new_move()

def r1_c1():
    if(button_r1_c1["text"]==empty):
        valid_move(button_r1_c1, 0)

def r1_c2():
    if(button_r1_c2["text"]==empty):
        valid_move(button_r1_c2, 1)

def r1_c3():
    if(button_r1_c3["text"]==empty):
        valid_move(button_r1_c3, 2)

def r2_c1():
    if(button_r2_c1["text"]==empty):
        valid_move(button_r2_c1, 3)

def r2_c2():
    if(button_r2_c2["text"]==empty):
        valid_move(button_r2_c2, 4)

def r2_c3():
    if(button_r2_c3["text"]==empty):
        valid_move(button_r2_c3, 5)

def r3_c1():
    if(button_r3_c1["text"]==empty):
        valid_move(button_r3_c1, 6)

def r3_c2():
    if(button_r3_c2["text"]==empty):
        valid_move(button_r3_c2, 7)

def r3_c3():
    if(button_r3_c3["text"]==empty):
        valid_move(button_r3_c3, 8)

def check_game_status():
    player_win = False
    player_tie = False
    if board[0].type == player and board[1].type == player and board[2].type == player:
        player_win = player
    if board[3].type == player and board[4].type == player and board[5].type == player:
        player_win = player
    if board[6].type == player and board[7].type == player and board[8].type == player:
        player_win = player
    if board[0].type == player and board[3].type == player and board[6].type == player:
        player_win = player
    if board[1].type == player and board[4].type == player and board[7].type == player:
        player_win = player
    if board[2].type == player and board[5].type == player and board[8].type == player:
        player_win = player
    if board[0].type == player and board[4].type == player and board[8].type == player:
        player_win = player
    if board[2].type == player and board[4].type == player and board[6].type == player:
        player_win = player
    if taken_positions >= 9:
        player_tie = True
    create_message(player_win, player_tie)

def create_message(player_win, player_tie):
    if player_win != False:
        if player_win == user:
            formal_end_game("Congratulations, you won!")
        else:
            formal_end_game("Sorry, you lost!")
    else:
        if player_tie != False:
            formal_end_game("We have a tie!")

#game buttons
button_r1_c1 = Button(game, text = empty, font = font1, command=r1_c1)
button_r1_c2 = Button(game, text = empty, font = font1, command=r1_c2)
button_r1_c3 = Button(game, text = empty, font = font1, command=r1_c3)
button_r2_c1 = Button(game, text = empty, font = font1, command=r2_c1)
button_r2_c2 = Button(game, text = empty, font = font1, command=r2_c2)
button_r2_c3 = Button(game, text = empty, font = font1, command=r2_c3)
button_r3_c1 = Button(game, text = empty, font = font1, command=r3_c1)
button_r3_c2 = Button(game, text = empty, font = font1, command=r3_c2)
button_r3_c3 = Button(game, text = empty, font = font1, command=r3_c3)
button_quit = Button(game, text = "Quit Game", font = font2, command=game.destroy)

button_restart = Button(game, text = "Restart Game", font = font2, command=reset_board) #here

player = user #setting current player turn

start() #call first function

game.mainloop()