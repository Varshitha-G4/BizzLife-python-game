from tkinter import *
from PIL import Image, ImageTk  # Import the Image module from the PIL (Pillow) library
import random


def dice_click():
    window1 = Toplevel()       #more than one tk() cant be used. hence, toplevel
    window1.geometry("230x230")
    window1.title("Dice")


    dice = ["dice_1.png", "dice_2.png","dice_3.png", "dice_4.png", "dice_5.png", "dice_6.png"]
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))  # Use ImageTk.PhotoImage

    label1 = Label(window1, image=image1)
    label1.place(x=35, y=47)

    window1.after(2300, lambda: window1.destroy()) #exits the window after 2800 milliseconds


    window1.mainloop()






