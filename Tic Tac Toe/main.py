
from tkinter import *
import tkinter.messagebox as messagebox

def callback(r ,c ): 
    global player 

    if player == 'X' and states[r][c] == 0 and game_stop == False :
        matrix[r][c].config(text='X' , fg = '#cd864a' , bg = '#282b2f' ) 
        states[r][c] = 'X'
        player = 'O' 

    if player == 'O' and states[r][c] == 0 and game_stop == False : 
        matrix[r][c].config(text='O' , fg = '#cd864a' , bg = '#282b2f' ) 
        states[r][c] = 'O'
        player = 'X' 

    winner()
    if game_stop == True and player == 'O' :
        messagebox.showinfo('Congrats' , 'player X won')

    elif game_stop == True and player == 'X' :
        messagebox.showinfo('Congrats' , 'player O won')
    


def winner(): 
    global game_stop 
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] !=0 : 
            matrix[i][0].config(bg = '#909a92') 
            matrix[i][1].config(bg = '#909a92') 
            matrix[i][2].config(bg = '#909a92') 
            game_stop = True

    for j in range(3):
        if states[0][j] == states[1][j] == states[2][j] !=0: 
            matrix[0][j].config(bg = '#909a92') 
            matrix[1][j].config(bg = '#909a92') 
            matrix[2][j].config(bg = '#909a92') 
            game_stop = True

        if states[0][0] == states[1][1] == states[2][2] !=0 : 
            matrix[0][0].config(bg = '#909a92') 
            matrix[1][1].config(bg = '#909a92') 
            matrix[2][2].config(bg = '#909a92') 
            game_stop = True

        if states[0][2] == states[1][1] == states[2][0] !=0: 
            matrix[0][2].config(bg = '#909a92') 
            matrix[1][1].config(bg = '#909a92') 
            matrix[2][2].config(bg = '#909a92') 
            game_stop = True



    
root = Tk()
root.title(' window ')

matrix = [[ 0,0,0] ,
          [ 0,0,0 ] ,
          [ 0,0,0 ] ]

states  = [ [ 0,0,0] ,
            [ 0,0,0 ] ,
            [ 0,0,0 ] ]


for i in range(3):
    for j in range(3):
        matrix[i][j] = Button( font = ( 'Arial', 60) , width= 4 , bg = '#cd864a' ,
                                 command  = lambda r=i , c=j :callback(r, c))

        matrix[i][j].grid(row=i , column=j)

player = 'X' 

game_stop = False 

mainloop() 
