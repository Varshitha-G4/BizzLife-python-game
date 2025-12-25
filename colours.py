from tkinter.colorchooser import askcolor
from tkinter import *

def choose_color(master):
    color = askcolor(title="Choose Background Color", color=master.cget("bg"))[1]
    if color:
        master.configure(bg=color)






