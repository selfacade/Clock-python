from tkinter import * 
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('clock')

def time() : 
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('Roboto', 40, 'normal'),
                      background='black',
                      foreground='green')

lbl.pack(anchor='center')
time()

mainloop()