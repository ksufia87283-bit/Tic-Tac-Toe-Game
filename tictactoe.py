# import tkinter as tk
# from tkinter import messagebox


# # Create main window
# root = tk.Tk()
# root.title("Tic Tac Toe")


# # Game variables
# player = "X"
# board = [""] * 9


# # Function to check winner
# def check_winner():
#     win_combinations = [
#         (0, 1, 2),
#         (3, 4, 5),
#         (6, 7, 8),
#         (0, 3, 6),
#         (1, 4, 7),
#         (2, 5, 8),
#         (0, 4, 8),
#         (2, 4, 6)
#     ]
#     for a, b, c in win_combinations:
#         if board[a] == board[b] == board[c] != "":
#             return board[a]
#     if "" not in board:
#         return "Draw"
#     return None


# # Button click handler
# def on_click(i):
#     global player
#     if board[i] == "" and not check_winner():
#         board[i] = player
#         buttons[i].config(text=player)
#         winner = check_winner()
#         if winner:
#             if winner == "Draw":
#                 messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
#             else:
#                 messagebox.showinfo("Tic Tac Toe", f"Player {winner} Wins!")
#         player = "O" if player == "X" else "X"


# # Reset game
# def reset_board():
#     global board, current_player
#     board = [""] * 9
#     current_player = "X"
#     for button in buttons:
#         button.config(text="")


# # Create buttons for the 3x3 grid
# buttons = []
# for i in range(9):
#     button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
#                        command=lambda i=i: on_click(i))
#     button.grid(row=i//3, column=i%3)
#     buttons.append(button)


# # Reset button
# reset_btn = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_board)
# reset_btn.grid(row=3, column=0, columnspan=3)


# root.mainloop()


#doneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


# # Create main window
# import tkinter as tk
# from tkinter import messagebox
# root=tk.Tk()
# root.title("Tic Tac Toe")
# # Game variables
# player="X"
# board=[""]*9
# # Function to check winner
# def check_winner():
    # win_combinations=[
    #     (0, 1, 2),
    #     (3, 4, 5),
    #     (6, 7, 8),
    #     (0, 3, 6),
    #     (1, 4, 7),
    #     (2, 5, 8),
    #     (0, 4, 8),
    #     (2, 4, 6)]
#     for a,b,c in win_combinations:
#         if board[a]==board[b]==board[c]!="":
#             return board[a]
#     if "" not in board:
#         return "Draw"
#     return None
# # Button click handler
# def onclick(i):
#     global player
#     if board[i]=="" and not check_winner():
#         board[i]=player
#         buttons[i].config(text=player)
#         winner=check_winner()
#         if winner:
#             if winner=="Draw":
#                 messagebox.showinfo("Tic Tac Toe","It's a Draw!")
#             else:
#                 messagebox.showinfo("Tic Tac Toe",f"Player {winner} wins!")
#         player = "O" if player == "X" else "X"
# # Reset game
# def reset_board():
#     global player,board
#     board=[""]*9
#     player="X"
#     for button in buttons:
#         button.config(text="")
# # Create buttons for the 3x3 grid
# buttons=[]
# for i in range(9):
#     button=tk.Button(root,text="", font=("Arial",25),width=5,height=2,command=lambda i=i:onclick(i))
#     button.grid(row=i//3,column=i%3)
#     buttons.append(button)
# # Reset button
# resetbut=tk.Button(root, text="Reset",font=("Arial",14),command=reset_board)
# resetbut.grid(row=3,column=0,columnspan=5)
# root.mainloop()

import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Tic Tac Toe")
player="X"
board=[""]*9
def check_winner():
    win_combinations=[
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)]
    for a,b,c in win_combinations:
        if board[a]==board[b]==board[c]!="":
            return board[a]
    if "" not in board:
        return "Draw"
    return None
buttons=[]
def on_click(i):
    global player
    if board[i]=="" and not check_winner():
        board[i]=player
        buttons[i].config(text=player)
        winner=check_winner()
        if winner:
            if winner=="Draw":
                messagebox.showinfo("Tic Tac Toe","Its a draw")
            else:
                messagebox.showinfo("Tic Tac Toe",f"Player {winner} wins!")
    player="O" if player=="X" else "X"
def reset_board():
    global player,board
    board=[""]*9
    player="X"
    for button in buttons:
        button.config(text="")
        
