from tkinter import *
def click_rules():
    win=Toplevel()
    cv=Canvas(win, height=730, width=990)
    filename=PhotoImage(file="images\Rules.png")
    image=cv.create_image(10, 10, anchor=NW, image=filename)
    cv.pack()
    win.mainloop()
