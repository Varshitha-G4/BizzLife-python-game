from tkinter import *



namelist=["player1","player2"]


def score(screen, namelist, money, initial_money,name, buyorsell, amount, money_labels):

  
    index = namelist.index(name)
    if buyorsell == "ADD":
        amountadded = int(money[index]) + int(amount)
        money[index] = amountadded
    elif buyorsell == "DEDUCT":
        amountadded = int(money[index]) - int(amount)
        money[index] = amountadded
    placey = 80
    for i, money_value in enumerate(money):
        money_labels[i].config(text=str(money_value))

        placey += 35
