# tkinter graphics tk main bart of tkinter, button is just a button and diabled is a boulan function
import random
import time
from tkinter import Tk, Button, DISABLED

def show_symbol(x,y):
    global first
    global previousX, previousY
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first:
        previousX = x
        previousY = y
        first = False
    elif previousX != x or previousY != y:
        if buttons[previousX,previousY]['text'] != buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previousX,previousY]['text'] = ''
            buttons[x,y]['text'] = ''
        else:
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True

root = Tk()
root.title("Rose")
root.resizable(width=True, height=True)
buttons={}
first = True
previousX = 0
previousY = 0

button_symbols = {}
symbols = [ 'A', 'A', 'K' , 'K', 'Q','Q',
           'J', 'J', '10' , '10', '9','9',
           '8', '8', '7' , '7', '6','6',
           '5', '5', '4' , '4', '3','3',]
random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbol(x,y,), width = 30 , height = 10 )
        button.grid(column=x, row=y)
        buttons[x,y] = button
        button_symbols[x,y] = symbols.pop()
root.mainloop()
