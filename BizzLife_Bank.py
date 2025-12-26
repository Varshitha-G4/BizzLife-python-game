from tkinter import *

import money_update
def click_balance():

    def gamescreen(namelist):
        screen=Toplevel()
        screen.geometry("450x450")
        screen.resizable(False,False)

        titlelabel=Label(screen,text="BizzLife Bank",font="bold, 20")
        titlelabel.place(x=110,y=14)


        placey=80
        initial_money= 50000
        money = money_update.money
        
        money_labels = []

        for j in namelist:
            namedroplabels=Label(screen,text=j,font="bold,16")
            namedroplabels.place(x=20,y=placey)            #y is for better spacing between each name

            moneydroplabel=Label(screen,text=money[namelist.index(j)],font="bold,16")
            moneydroplabel.place(x=200,y=placey)

            money_labels.append(moneydroplabel) #to prevent overwriting

            bizzlabel=Label(screen,text="Bizz",font="italic")
            bizzlabel.place(x=270,y=placey)

            placey+=35                                  #distance between each player gets added

        namedropdownlabel=Label(screen,text="Select Player",font="bold,11")
        namedropdownlabel.place(x=20,y=310)

        selectedname=StringVar()
        selectedname.set("player name")
        drop=OptionMenu(screen,selectedname,*namelist)
        drop.place(x=160,y=310)

        add_button = Button(screen, text="ADD", font="bold", bg="#26dc93",
                            command=lambda: money_update.score(screen, namelist, money, initial_money,
                                                                selectedname.get(), "ADD", amount.get(), money_labels))
        add_button.place(x=160, y=390)
        deduct_button = Button(screen, text="DEDUCT", font="bold", bg="#f15874",
                               command=lambda: money_update.score(screen, namelist, money, initial_money, 
                                                                  selectedname.get(), "DEDUCT", amount.get(), money_labels))
        deduct_button.place(x=250, y=390)
        amountLabel=Label(screen,text="Amount",font="bold,11")
        amountLabel.place(x=20,y=350)


        amount=Entry(screen,borderwidth=5,highlightthickness=0)
        amount.place(x=160,y=350)


    gamescreen(money_update.namelist)


