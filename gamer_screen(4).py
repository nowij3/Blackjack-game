import tkinter
from tkinter import Image
import Deck as deck
import CardLabel
import sys
import os

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
import tkinter
from tkinter import Image
import Deck as deckimport tkinter
from tkinter import Image
import Deck as deck
import CardLabel
import Gamer
import Dealer
import User
import CountingPlayer
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
     
                self.a1=tkinter.Button(window, text="Easy", command=self.Easy)
                self.a1.place(x=220, y=50, width=200, height=70)

                self.a2=tkinter.Button(window, text="Normal", command=self.Normal)
                self.a2.place(x=220, y=150, width=200, height=70)

                self.a3=tkinter.Button(window, text="Hard", command=self.Hard)
                self.a3.place(x=220, y=250, width=200, height=70)


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


        def Easy(self):
                a1=tkinter.Button(window, text="Deal")
                a2=tkinter.Button(window, text="Hit")
                a3=tkinter.Button(window, text="Stand")
                a4=tkinter.Button(window, text="New Hand")
                a5=tkinter.Button(window, text="1000", command=lambda:chip_pressed('1000'))
                a6=tkinter.Button(window, text="500", command=lambda:chip_pressed('500'))
                a7=tkinter.Button(window, text="200", command=lambda:chip_pressed('200'))
                a8=tkinter.Label(window, text="Balance :")
                a9=tkinter.Button(window, text="New Game")
                p1=tkinter.Label(window, text="Dealer", bg="white")
                p2=tkinter.Label(window, text="Player1", bg="white")
                p3=tkinter.Label(window, text="Player2", bg="white")

                a1.place(x=150, y=300, width=90, height=50)
                a2.place(x=300, y=300, width=90, height=50)
                a3.place(x=450, y=300, width=90, height=50)
                a4.place(x=20, y=30, width=80, height=40)
                a5.place(x=20, y=90, width=50, height=50)
                a6.place(x=20, y=150, width=50, height=50)
                a7.place(x=20, y=210, width=50, height=50)
                a8.place(x=20, y=320, width=50, height=30)
                a9.place(x=20, y=10, width=80, height=30)
                p1.place(x=300, y=25, width=70, height=30)
                p2.place(x=120, y=150, width=70, height=30)
                p3.place(x=500, y=150, width=70, height=30)

                def chip_pressed(value):
    
                    num_entry.insert("end", value)  
                    print(value,"pressed")


                entry_value=tkinter.StringVar(window, value='')

                num_entry=tkinter.Entry(window, textvariable=entry_value, width=10)
                num_entry.grid(row=0, columnspan=1)
                num_entry.place(x=20, y=290)

import CardLabel
import Gamer
import Dealer
import User
import CountingPlayer
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
     
                self.a1=tkinter.Button(window, text="Easy", command=self.Easy)
                self.a1.place(x=220, y=50, width=200, height=70)

                self.a2=tkinter.Button(window, text="Normal", command=self.Normal)
                self.a2.place(x=220, y=150, width=200, height=70)

                self.a3=tkinter.Button(window, text="Hard", command=self.Hard)
                self.a3.place(x=220, y=250, width=200, height=70)


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


        def Easy(self):
                a1=tkinter.Button(window, text="Deal")
                a2=tkinter.Button(window, text="Hit")
                a3=tkinter.Button(window, text="Stand")
                a4=tkinter.Button(window, text="New Hand")
                a5=tkinter.Button(window, text="1000", command=lambda:chip_pressed('1000'))
                a6=tkinter.Button(window, text="500", command=lambda:chip_pressed('500'))
                a7=tkinter.Button(window, text="200", command=lambda:chip_pressed('200'))
                a8=tkinter.Label(window, text="Balance :")
                p1=tkinter.Label(window, text="Dealer", bg="white")
                p2=tkinter.Label(window, text="Player1", bg="white")
                p3=tkinter.Label(window, text="Player2", bg="white")

                a1.place(x=150, y=300, width=90, height=50)
                a2.place(x=300, y=300, width=90, height=50)
                a3.place(x=450, y=300, width=90, height=50)
                a4.place(x=20, y=30, width=80, height=40)
                a5.place(x=20, y=90, width=50, height=50)
                a6.place(x=20, y=150, width=50, height=50)
                a7.place(x=20, y=210, width=50, height=50)
                a8.place(x=20, y=320, width=50, height=30)
                p1.place(x=300, y=25, width=70, height=30)
                p2.place(x=120, y=150, width=70, height=30)
                p3.place(x=500, y=150, width=70, height=30)

                def chip_pressed(value):
    
                    num_entry.insert("end", value)  
                    print(value,"pressed")


                entry_value=tkinter.StringVar(window, value='')

                num_entry=tkinter.Entry(window, textvariable=entry_value, width=10)
                num_entry.grid(row=0, columnspan=1)
                num_entry.place(x=20, y=290)
