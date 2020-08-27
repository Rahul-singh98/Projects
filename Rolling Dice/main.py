from tkinter import *
from PIL import ImageTk , Image
import random 


root = Tk()
root.geometry('1200x700')
root.title('Rolling Dice')

ct = [random.randrange(256) for x in range(3)]
brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2] ))
root.configure(bg = 'white' if brightness < 120 else 'Black' )


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


button = Button(root , text= 'Roll Dice' , fg='white', bg= "#660000",command = roll_dice)

button.pack(side=BOTTOM)

root.mainloop()