
import tkinter as tk
from tkinter import messagebox

def on_button_click(row, col):
    if board[row][col] == '':
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_board()
        else:
            toggle_player()
            # Change color of player X to blue and player O to red
            if current_player == "X":
                buttons[row][col].config(fg="blue")
            else:
                buttons[row][col].config(fg="red")

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        elif board[0][i] == board[1][i] == board[2][i] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

def check_draw():
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True

def reset_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = ''
            buttons[i][j].config(text="")
    global current_player
    current_player = "X"

def toggle_player():
    global current_player
    current_player = {"X": "O", "O": "X"}[current_player]


root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"

board = [[''] * 3 for _ in range(3)]
buttons = [[''] * 3 for _ in range(3)]


for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Comic Sans Ms",50), width=4, height=1,command=lambda i=i, j=j: on_button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()

