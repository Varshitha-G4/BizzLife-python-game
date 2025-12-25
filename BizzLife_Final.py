
from tkinter import *
import Dice
import BizzLife_Bank
import message_collect
import message_pay
import BizzLife_Buttons
import BizzLife_pointers
import BizzLife_Rules
import pointer_movement
import messages
from colours import choose_color



class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("BizzLife")
        self.master.geometry("1568x1010")

        BizzLife_Buttons.create_buttons(self)
        BizzLife_pointers.create_pointers(self)

        master.bind("<Right>", lambda event: pointer_movement.move_pointer(self,"right", self.pointer1))
        master.bind("<Left>", lambda event: pointer_movement.move_pointer(self, "left", self.pointer1))
        master.bind("<d>", lambda event:pointer_movement.move_pointer(self,"right", self.pointer2))
        master.bind("<a>", lambda event: pointer_movement.move_pointer(self, "left", self.pointer2))


        color_button = Button(bg="#26dc93", fg="#000000", command=self.choose_color, font=("Comic Sans", 14),
                              text="CHOOSE COLOR", activebackground="#26bedc")
        color_button.place(x=740, y=742)
    def choose_color(self):
        choose_color(self.master)

    def button_click(self, button_number):

        if button_number == 3:
           message_collect.click_c(messages.c1)
        if button_number == 6:
            message_pay.click_p(messages.p1)
        if button_number == 9:
           message_collect.click_c(messages.c2)
        if button_number == 12:
            message_pay.click_p(messages.p2)
        if button_number == 15:
           message_collect.click_c(messages.c3)
        if button_number == 18:
            message_pay.click_p(messages.p3)
        if button_number == 21:
           message_collect.click_c(messages.c4)
        if button_number == 24:
            message_pay.click_p(messages.p4)
        if button_number == 27:
           message_collect.click_c(messages.c5)
        if button_number == 30:
            message_pay.click_p(messages.p5)
        if button_number == 33:
           message_collect.click_c(messages.c6)
        if button_number == 36:
            message_pay.click_p(messages.p6)
        if button_number == 39:
            message_pay.click_p(messages.p7)
        if button_number == 42:
           message_collect.click_c(messages.c7)
        if button_number == 45:
            message_pay.click_p(messages.p8)
        if button_number == 48:
           message_collect.click_c(messages.c8)
        if button_number == 51:
            message_pay.click_p(messages.p9)
        if button_number == 54:
            message_pay.click_p(messages.p10)



if __name__ == "__main__":
    root = Tk()
    game = Game(root)

    dice_button = Button(bg="#26dc93", fg="#000000", command=Dice.dice_click, font=("Comic Sans", 14), text="ROLL",activebackground="#26bedc")
    dice_button.place(x=130, y=742)

    rules_button = Button(bg="#26dc93", fg="#000000",command=BizzLife_Rules.click_rules, font=("Comic Sans", 14), text="RULES",activebackground="#26bedc")
    rules_button.place(x=550, y=742)

    bank_button = Button(bg="#26dc93", fg="#000000", command=BizzLife_Bank.click_balance, font=("Comic Sans", 14),text="BALANCE", activebackground="#26bedc")
    bank_button.place(x=320, y=742)


    root.mainloop()

