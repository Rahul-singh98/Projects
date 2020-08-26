from tkinter import *
from PIL import ImageTk , Image
import random 

root = Tk()
root.geometry('200x200')
root.title('Rolling Dice')

dice = ['./Dice_Images/Dice1.png','./Dice_Images/Dice2.png',
        './Dice_Images/Dice3.png','./Dice_Images/Dice4.png',
        './Dice_Images/Dice5.png','./Dice_Images/Dice6.png']

image = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label = Label(root , image= image)
label.pack()

def roll_dice():
    image = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label.configure(image= image)
    label.image =image


button = Button(root , text= 'Roll Dice' , fg='black',command = roll_dice)

button.pack(side=BOTTOM)

root.mainloop()