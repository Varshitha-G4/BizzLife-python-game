
import tkinter
from tkinter import *
#CREATING FUNCTION FOR COLLECTING MONEY
def click_c(m1):
    message=Tk()
    message.title("bizzlife")
    message.geometry("275x250")
    message.resizable(False,False)
    message.configure(bg='#FFD52E')
    l1=Label(message,text=m1,font=('Courier', 18, "bold italic",),bg='#FFD52E')
    l1.place(relx=0.5, rely=0.5, anchor=CENTER)
    message.after(2300, lambda: message.destroy())
    message.mainloop()


#CREATING FUNCTION FOR PAYING MONEY
