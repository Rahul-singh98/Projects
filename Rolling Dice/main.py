from tkinter import *
import random 

root = Tk()
root.geometry('400x400')
root.title('Rolling Dice')

label = Label(root , text='' , font={'Helvetica' , 200})


def roll_dice():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()

button = Button(root , text= 'Roll Dice' , fg='black',command = roll_dice)

button.pack()

root.mainloop()