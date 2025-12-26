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
        money=[]
        for i in namelist:
            money.append(initial_money)             #EACH PLAYER WILL HAVE INITIAL MONEY ADDED TO THE LIST
        money_labels = []

        for j in namelist:
            namedroplabels=Label(screen,text=j,font="bold,16")
            namedroplabels.place(x=20,y=placey)            #y is for better spacing between each name

            moneydroplabel=Label(screen,text=initial_money,font="bold,16")
            moneydroplabel.place(x=200,y=placey)

            money_labels.append(moneydroplabel) #to prevent overwriting

            bizzlabel=Label(screen,text="Bizz",font="italic")
            bizzlabel.place(x=270,y=placey)

            placey+=35                                  #distance between each player gets added

        namedropdownlabel=Label(screen,text="Select Player",font="bold,11")
        namedropdownlabel.place(x=20,y=320)

        selectedname=StringVar()
        selectedname.set("player name")
        drop=OptionMenu(screen,selectedname,*namelist)
        drop.place(x=160,y=323)

        buyorsellLabel=Label(screen,text="Enter Option",font="bold,11")
        buyorsellLabel.place(x=20,y=350)

        buyorsell=StringVar()
        buyorsell.set("select option")
        buysorsell=["ADD","DEDUCT"]
        buyorsells=OptionMenu(screen,buyorsell,*buysorsell)
        buyorsells.place(x=160,y=353)

        amountLabel=Label(screen,text="Amount",font="bold,11")
        amountLabel.place(x=20,y=380)


        amount=Entry(screen,borderwidth=5,highlightthickness=0)
        amount.place(x=160,y=390)

        #added money_labels
        button=Button(screen,text="SUBMIT",font="bold",command=lambda:money_update.score(screen,namelist,money,initial_money,selectedname.get(),buyorsell.get(),amount.get(), money_labels),border=1,height=1)
        button.place(x=350,y=400)


    gamescreen(money_update.namelist)


