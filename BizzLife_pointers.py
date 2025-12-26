from tkinter import *
from colours import choose_color
def create_pointers(self):

    self.pointer1_position = 0
    self.pointer1 = Label(self.master, text="P1", font=("Arial", 16), fg="#ffffff",bg="red")
    self.pointer1.place(x=5,y=624)

    self.pointer2_position = 0
    self.pointer2 = Label(self.master, text="P2", font=("Arial", 16), fg="#ffffff",bg="blue")
    self.pointer2.place(x=61, y=669)