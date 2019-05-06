import tkinter
from tkinter import Image
import Deck as deck
import CardLabel
import sys
import os

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)


class Blackjack:

    def __init__(self):
        self.window=tkinter.Tk()
        self.window.title("BlackJack Game")
        self.window.geometry("640x400+100+100")
        self.window.resizable(True, True)

        label = tkinter.Label(window, text="Welcome to BlackJack World")
        label.pack()
     
        self.a1=tkinter.Button(window, text="Easy", command=Easy)
        self.a1.place(x=220, y=50, width=200, height=70)

        self.a2=tkinter.Button(window, text="Normal", command=Normal)
        self.a2.place(x=220, y=150, width=200, height=70)

        self.a3=tkinter.Button(window, text="Hard", command=Hard)
        self.a3.place(x=220, y=250, width=200, height=70)

        self.chip=tkinter.PhotoImage(file="casino-chip.gif")
        self.lbl=tkinter.Label(self.window,image=chip)
        self.lbl.image=chip
        self.lbl.place(x=20,y=20)
        self.lbl.image=chip.subsample(1000,1000)

        self.b1=tkinter.Button(window, text="Deal", command=Deal)
        self.b2=tkinter.Button(window, text="Stand", command=Stand)
        self.b3=tkinter.Button(window, text="Hit", command=Hit)
        self.b4=tkinter.Button(window, text="New Hand", command=NewHand)



        self.a4.place(x=150, y=300, width=90, height=50)
        self.a5.place(x=300, y=300, width=90, height=50)
        self.a6.place(x=450, y=300, width=90, height=50)
        self.a7.place(x=20, y=30, width=80, height=40)

        CardLabel.load_images()
        self._dealercard=[CardLabel(self.root) for i in range(6)]
        self._playercard1=[CardLabel(self.root) for i in range(6)]
        self._playercard2=[CardLabel(self.root) for i in range(6)]
        self._usercard=[CardLabel(self.root) for i in range(6)]

        dealerpos=0
        for x in self._dealercard:
                x.grid(row=0, column=dealerpos)
                x.dispaly(side='blank')
                dealerpos+=1

        playerpos_1=0
        for y in self._playercard1:
                x.grid(row=0, column=playerpos_1)
                x.dispaly(side='blank')
                playerpos_1+=1

        playerpos_2=0
        for z in self._playercard2:
                x.grid(row=0, column=playerpos_2)
                x.dispaly(side='blank')
                playerpos_2+=1

        userpos=0
        for w in self._usercard:
                x.grid(row=0, column=userpos)
                x.dispaly(side='blank')
                userpos+=1

             
        self.window.mainloop()
