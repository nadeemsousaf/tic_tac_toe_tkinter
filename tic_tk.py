from tkinter import * 

game = Tk()
game.geometry("400x400")

canvas = Canvas(game, width=400, height=400)
font1 = ("Arial", 40, "bold")

player_move = 'x'
empty = ' '


board = []

class square:
    def __init__(self, type, x_num, y_num):
        self.type = type
        self.x_num = x_num
        self.y_num = y_num
        
def create_board():
    #global board
    board.append(square(empty,600,250))
    board.append(square(empty,800,250))
    board.append(square(empty,1000,250))
    board.append(square(empty,600,450))
    board.append(square(empty,800,450))
    board.append(square(empty,1000,450))
    board.append(square(empty,600,650))
    board.append(square(empty,800,650))
    board.append(square(empty,1000,650))

def update_board():
    for i in board:
        if i.type != empty:
            if i.type == 'X':
                canvas.create_window(i.x_num, i.y_num, window = button_x)
            else:
                canvas.create_window(i.x_num, i.y_num, window = button_o)


def opponent_move():
    global player_move
    player_move = 'O'

def user_move():
    global player_move
    player_move = 'X'

def opponent_play(): #generate opponent move
    ok = 1

def start():
    create_board()
    canvas.pack(fill="both", expand=True)
    canvas.create_window(600, 250, window = button_r1_c1)
    canvas.create_window(800, 250, window = button_r1_c2)
    canvas.create_window(1000, 250, window = button_r1_c3)
    canvas.create_window(600, 450, window = button_r2_c1)
    canvas.create_window(800, 450, window = button_r2_c2)
    canvas.create_window(1000, 450, window = button_r2_c3)
    canvas.create_window(600, 650, window = button_r3_c1)
    canvas.create_window(800, 650, window = button_r3_c2)
    canvas.create_window(1000, 650, window = button_r3_c3)

def r1_c1():
    board[0].type = player_move

def r1_c2():
    board[1].type = player_move

def r1_c3():
    board[2].type = player_move

def r2_c1():
    board[3].type = player_move

def r2_c2():
    board[4].type = player_move

def r2_c3():
    board[5].type = player_move

def r3_c1():
    board[6].type = player_move

def r3_c2():
    board[7].type = player_move

def r3_c3():
    board[8].type = player_move

#game buttons
button_r1_c1 = Button(game, text = "   ", font = font1, command=r1_c1)
button_r1_c2 = Button(game, text = "   ", font = font1, command=r1_c2)
button_r1_c3 = Button(game, text = "   ", font = font1, command=r1_c3)
button_r2_c1 = Button(game, text = "   ", font = font1, command=r2_c1)
button_r2_c2 = Button(game, text = "   ", font = font1, command=r2_c2)
button_r2_c3 = Button(game, text = "   ", font = font1, command=r2_c3)
button_r3_c1 = Button(game, text = "   ", font = font1, command=r3_c1)
button_r3_c2 = Button(game, text = "   ", font = font1, command=r3_c2)
button_r3_c3 = Button(game, text = "   ", font = font1, command=r3_c3)
button_x = Button(game, text = " X ", font = font1)
button_o = Button(game, text = " O ", font = font1)
button_quit = Button(game, text = "Quit Game", font = font1, command=game.destroy)

start()

game.mainloop()