from tkinter import *

# main window
root = Tk()

# geometry of window
root.geometry('400x380')
root.resizable(0,0)

root.title("Calculator")

# first button
def btn_click(item):
    '''
        this button is used to update text field whenever any input is provided
    '''
    global expression 
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    """
        this function is used to clear the earlier expression and calculations using 'C'
    """
    global expression 
    expression = ''
    input_text.set('')

def btn_equal():
    """
        this function is used to evaluate expression
    """
    global expression 
    result = str(eval(expression))
    input_text.set(result)
    expression = ''

expression = ""

input_text = StringVar()

# Create a frame
input_frame = Frame(root , width= 312 , height= 50 , bd = 0 , highlightbackground = "black" ,
                    highlightcolor = "black"  , highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame , font = ('arial' , 18 , 'bold') , textvariable= input_text , 
                        width = 50 , bg = "#eee" , bd = 0 , justify = RIGHT)
input_field.grid(row = 0 , column = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(root , width= 312 , height = 272.5 , bg = "grey")
btns_frame.pack()

# first row
clear = Button(btns_frame , text = "C" , bg= '#eee' , fg = 'black' , width = 37 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_clear()).grid(row= 0 , column= 0 ,
                                                                        columnspan=3 , padx = 1 , pady =1)

divide = Button(btns_frame , text = "/" , bg= '#eee' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('/')).grid(row= 0 , column= 3 ,
                                                                     padx = 1 , pady =1)
seven = Button(btns_frame , text = "7" , bg= '#fff' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('7')).grid(row= 1 , column= 0 ,
                                                                     padx = 1 , pady =1)
eight = Button(btns_frame , text = "8" , bg= '#fff' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('8')).grid(row= 1 , column= 1 ,
                                                                     padx = 1 , pady =1)
nine = Button(btns_frame , text = "9" , bg= '#fff' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('9')).grid(row= 1 , column= 2 ,
                                                                     padx = 1 , pady =1) 

multiply = Button(btns_frame , text = "*" , bg= '#eee' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('*')).grid(row= 1 , column= 3 ,
                                                                     padx = 1 , pady =1)  

# Second row
four = Button(btns_frame , text = "4" , bg= '#fff' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('4')).grid(row= 2 , column= 0 ,
                                                                     padx = 1 , pady =1) 

five = Button(btns_frame , text = "5" , bg= '#fff' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('5')).grid(row= 2 , column= 1 ,
                                                                     padx = 1 , pady =1) 

six = Button(btns_frame , text = "6" , bg= '#fff' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('6')).grid(row= 2 , column= 2 ,
                                                                     padx = 1 , pady =1) 

minus = Button(btns_frame , text = "-" , bg= '#eee' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('-')).grid(row= 2 , column= 3 ,
                                                                     padx = 1 , pady =1) 

# third row
one = Button(btns_frame , text = "1" , bg= '#fff' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('1')).grid(row= 3 , column= 0 ,
                                                                     padx = 1 , pady =1) 

two = Button(btns_frame , text = "2" , bg= '#fff' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('2')).grid(row= 3 , column= 1 ,
                                                                     padx = 1 , pady =1) 

three = Button(btns_frame , text = "3" , bg= '#fff' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('3')).grid(row= 3 , column= 2 ,
                                                                     padx = 1 , pady =1) 

plus = Button(btns_frame , text = "+" , bg= '#eee' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('+')).grid(row= 3 , column= 3 ,
                                                                     padx = 1 , pady =1) 

# last row

zero = Button(btns_frame , text = "0" , bg= '#fff' , fg = 'black' , width = 23 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('0')).grid(row= 4 , column= 0 ,
                                                                     columnspan= 2, padx = 1 , pady =1) 

dot = Button(btns_frame , text = "." , bg= '#eee' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_click('.')).grid(row= 4 , column= 2 ,
                                                                     padx = 1 , pady =1) 

equal  = Button(btns_frame , text = "=" , bg= '#eee' , fg = 'black' , width = 10 , height= 3 , 
                bd = 0 , cursor = 'hand2' , command =lambda: btn_equal()).grid(row= 4 , column= 3 ,
                                                                     padx = 1 , pady =1) 



mainloop()
