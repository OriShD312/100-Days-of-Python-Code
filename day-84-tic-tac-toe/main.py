from time import time
from tkinter import *
from tkinter import messagebox
import numpy as np

N = 4
ROWS = N
COLS = N

game_board = np.zeros((ROWS, COLS), dtype=int)
current_player = 1

def check_winner():
    for i in range(N):
        if np.all(game_board[i,:] == game_board[i,0]) and game_board[i,0] != 0:
            messagebox.showinfo('Winner',f'Player {int(game_board[i,0])} Wins!')
            reset_game()
        if np.all(game_board[:,i] == game_board[0,i]) and game_board[0,i] != 0:
            messagebox.showinfo('Winner',f'Player {int(game_board[0,i])} Wins!')
            reset_game()
        
    if np.all(game_board.diagonal() == game_board[0,0]) and game_board[0,0] != 0:
        messagebox.showinfo('Winner',f'Player {int(game_board[0,0])} Wins!')
        reset_game()
    if np.all(np.fliplr(game_board).diagonal() == game_board[0,N-1]) and game_board[0,N-1] != 0:
        messagebox.showinfo('Winner',f'Player {int(game_board[0,N-1])} Wins!')
        reset_game()

    if np.all(game_board!=0):
        messagebox.showinfo('Tie', 'Its a Draw')
        reset_game()
        

def clicked(row, col):
    global current_player
    b = frame.grid_slaves(row=row, column=col)[0]
    if current_player == 1:
        b.config(text='X', state=DISABLED)
        game_board[row][col] = current_player
        current_player = 2
    elif current_player == 2:
        b.config(text='O', state=DISABLED)
        game_board[row][col] = current_player
        current_player = 1

    check_winner()
    
def reset_game():
    global frame, current_player, game_board
    game_board = np.zeros((ROWS, COLS))
    current_player = 1
    frame.destroy()
    frame = create_game_board(window)
    frame.pack()

def create_game_board(window):
    frame = Frame(window)
    frame.pack()

    for row in range(ROWS):
        for col in range(COLS):
            b = Button(frame, text='', font=('Arial', 50), width=6, height=2, command=lambda x=row, y=col: clicked(x, y))
            b.grid(row=row, column=col, sticky=NSEW)

    reset_button = Button(frame, text='Reset Game', command=reset_game)
    reset_button.grid(row=N, columnspan=N, sticky=EW, padx=5, pady=5)

    return frame

window = Tk()

frame = create_game_board(window)
frame.pack()

window.mainloop()
