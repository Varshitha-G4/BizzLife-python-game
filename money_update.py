from tkinter import *



namelist=["player1","player2"]


def score(screen, namelist, money, initial_money,name, buyorsell, amount):

  
    index = namelist.index(name)
    if buyorsell == "ADD":
        amountadded = int(money[index]) + int(amount)
        money[index] = amountadded
    elif buyorsell == "DEDUCT":
        amountadded = int(money[index]) - int(amount)
        money[index] = amountadded
    placey = 80
    for i in money:
        moneydroplabel = Label(screen, text=i, font="bold")
        moneydroplabel.place(x=200, y=placey)

        placey += 35
