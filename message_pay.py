from tkinter import *

def click_p(m2):
    message=Tk()
    message.title("bizzlife")
    message.geometry("275x250")
    message.resizable(False,False)
    message.configure(bg='#FFAF16')
    l1=Label(message,text=m2,font=('Courier', 18, "bold italic"),bg='#FFAF16')
    l1.place(relx=0.5, rely=0.5, anchor=CENTER)
    message.after(2300, lambda: message.destroy())
    message.mainloop()