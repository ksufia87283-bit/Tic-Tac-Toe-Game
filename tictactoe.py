import tkinter as tk

from tkinter import messagebox,simpledialog



#Game varible

player="X"

board=[""]*9

player1=simpledialog.askstring("player1","enter your name player 1: ")

player2=simpledialog.askstring("player2","enter your name player 2: ")

games_round=simpledialog.askinteger("games_round","How many rounds do you want to play?: ")

totalround=messagebox.showinfo("Tic Tac Toe",f"the total amount of rounds will be {games_round}")

winningpoint=messagebox.showinfo("Tic Tac Toe",f"the first to reach {games_round//2+1}, you will become a winner")

scoreX=0

scoreO=0



def update_score_label():

    name.config(text=f"{player1} (X): {scoreX}    |    {player2} (O): {scoreO}" )

#function to check the winner

def check_winner():

    win_combinations=[

        (0,1,2),

        (0,3,6),

        (0,4,8),

        (1,4,7),

        (2,5,8),

        (3,4,5),

        (2,4,6),

        (6,7,8)]

    for a,b,c in win_combinations:

        if board[a]==board[b]==board[c]!="":

            return board[a]

    if "" not in board:

        return "Draw"

    return None

#button clicker

def on_click(i):

    global player, scoreO,scoreX,games_round

    if board[i]=="" and not check_winner():

        board[i]=player    

        buttons[i].config(text=player)

        winner=check_winner()

        if winner:

            if winner=="Draw":

                messagebox.showinfo("Tic Tac Toe","Its a draw!")

            else:

               



                if winner=="X":

                    scoreX+=1

                    winnername=player1

                    update_score_label()

                    messagebox.showinfo('Tic Tac Toe',f"{winnername} ({winner}) wins!")

                    reset_board()

                    return

                else:

                    scoreO+=1

                    winnername=player2

                    update_score_label()

                    messagebox.showinfo('Tic Tac Toe',f"{winnername} ({winner}) wins!")

                    reset_board()

                    return

    player="O" if player=="X" else "X"

    if scoreX==games_round//2+1:

        messagebox.showinfo('Tic Tac Toe',f"{winnername} ({winner}) is the overall champion!")

    if scoreO==games_round//2+1:

        messagebox.showinfo('Tic Tac Toe',f"{winnername} ({winner}) is the overall champion!")

#create a main window

root=tk.Tk()

root.title("Tic Tac Toe")  

#create buttons for 3x3 grid

buttons=[]

for i in range(9):

    button=tk.Button(root, text="",font=("Arial",25),width=5, height=2, command=lambda i=i:on_click(i))

    button.grid(row=i//3,column=i%3)

    buttons.append(button)

#reset button

def reset_board():

    global player, board

    board=[""]*9

    player="X"

    for button in buttons:

        button.config(text="")

namerounds=tk.Label(root, text=f"Total rounds: {games_round} ", font=("Arial",14))

namerounds.grid(row=3,column=0,columnspan=3,pady=5)

name=tk.Label(root, text=f"{player1} (X): 0    |    {player2} (O): 0 ", font=("Arial",14))

name.grid(row=4,column=0,columnspan=3,pady=5)

reset_button=tk.Button(root, text="Reset", font=("Arial",14),width=5,height=0,command=reset_board)

reset_button.grid(row=5,column=0, columnspan=5,pady=5)



root.mainloop()
