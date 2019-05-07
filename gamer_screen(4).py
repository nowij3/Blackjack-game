import tkinter
from tkinter import Image
import Deck as deck
import CardLabel
import Gamer
import Dealerimport tkinter
from tkinter import Image
import Deck as deck
import DeckHandler
from CardLabel import CardLabel
import Gamer
import Dealer
import User
import CountingPlayer
import sys
import os
import Main

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)


class Blackjack:
        
        def __init__(self):
                self.window=tkinter.Tk()
                self.window.title("BlackJack Game")
                self.window.geometry("640x400+100+100")
                self.window.resizable(True, True)

                self.a1=tkinter.Button(self.window, text="Deal", command=self.Deal)
                self.a2=tkinter.Button(self.window, text="Hit", command=self.Hit)
                self.a3=tkinter.Button(self.window, text="Stand", command=self.Stand)
                self.a4=tkinter.Button(self.window, text="New Hand", command=self.NewHand)
                self.a5=tkinter.Button(self.window, text="1000", command=lambda:chip_pressed('1000'))
                self.a6=tkinter.Button(self.window, text="500", command=lambda:chip_pressed('500'))
                self.a7=tkinter.Button(self.window, text="200", command=lambda:chip_pressed('200'))
                self.a8=tkinter.Label(self.window, text="Balance :")
                self.p1=tkinter.Label(self.window, text="Dealer", bg="white")
                self.p2=tkinter.Label(self.window, text="Player1", bg="white")
                self.p3=tkinter.Label(self.window, text="Player2", bg="white")
                self.l1=tkinter.Button(self.window, text="Easy", command=self.Easy)
                self.l2=tkinter.Button(self.window, text="Normal", command=self.Normal)
                self.l3=tkinter.Button(self.window, text="Hard", command=self.Hard)


                self.a1.place(x=150, y=300, width=90, height=50)
                self.a2.place(x=300, y=300, width=90, height=50)
                self.a3.place(x=450, y=300, width=90, height=50)
                self.a4.place(x=20, y=50, width=80, height=30)
                self.a5.place(x=20, y=90, width=50, height=50)
                self.a6.place(x=20, y=150, width=50, height=50)
                self.a7.place(x=20, y=210, width=50, height=50)
                self.a8.place(x=20, y=320, width=50, height=30)
                self.p1.place(x=300, y=25, width=70, height=30)
                self.p2.place(x=120, y=150, width=70, height=30)
                self.p3.place(x=500, y=150, width=70, height=30)
                self.l1.place(x=20, y=10, width=70, height=30)
                self.l2.place(x=100, y=10, width=70, height=30)
                self.l3.place(x=180, y=10, width=70, height=30)

                def chip_pressed(value):



                    if not num_entry.get() == '':

                        v = int(value)

                        v += int(num_entry.get())

                        # value += int(num_entry.get())

                        num_entry.delete(0,'end')

                        num_entry.insert("end", str(v))

                    else:

                        num_entry.insert("end", value)

                    print(value,"pressed")
                    # print(int(num_entry.get()))


                entry_value=tkinter.StringVar(self.window, value='')

                num_entry=tkinter.Entry(self.window, textvariable=entry_value, width=10)
                num_entry.grid(row=0, columnspan=1)
                num_entry.place(x=20, y=290)
     
                CardLabel.load_images()
                self._dealercard=[CardLabel(self.window) for i in range(1)]
                self._playercard1=[CardLabel(self.window) for i in range(1)]
                self._playercard2=[CardLabel(self.window) for i in range(1)]
                self._usercard=[CardLabel(self.window) for i in range(1)]

                dealerpos=0
                for x in self._dealercard:
                        x.grid(row=0, column=1)
                        x.display(side='front')
                        dealerpos+=1

                playerpos_1=0
                for y in self._playercard1:
                        x.grid(row=1, column=1)
                        x.display(side='front')
                        playerpos_1+=1

                playerpos_2=0
                for z in self._playercard2:
                        x.grid(row=1, column=2)
                        x.display(side='front')
                        playerpos_2+=1

                userpos=0
                for w in self._usercard:
                        x.grid(row=2, column=1)
                        x.display(side='front')
                        userpos+=1

             
                self.window.mainloop()


        def Easy(self):
                
                Main.set_level("easy")
                self.Playing()

        def Normal(self):

                Main.set_level("normal")
                self.Playing()

        def Hard(self):

                Main.set_level("hard")
                self.Playing()

                

        def Playing(self):
                Main.user_betting(chip)
                Main.calculate_chip()
                Main.play_start()
                Main.make_players(name1, name2)

        def Deal(self):

                num_entry.config(state='disabled')
                self.dealer=self.deck.deal(2)
                self.player1=self.deck.deal(2)
                self.player2=self.deck.deal(2)
                self.user=self.deck.deal(2)

                self._dealercard[0].display(self, 'front', self.dealer[0]._id)
                self._dealercard[1].display(self, 'back', self.dealer[1]._id)

                self._player1card[0].display(self, 'front', self.dealer[0]._id)
                self._player1card[1].display(self, 'back', self.dealer[1]._id)

                self._player2card[0].display(self, 'front', self.dealer[0]._id)
                self._player2card[1].display(self, 'back', self.dealer[1]._id)

                self._usercard[0].display(self, 'front', self.dealer[0]._id)
                self._usercard[1].display(self, 'back', self.dealer[1]._id)

                Main.user_betting(chip)
                Main.play_deal()
                
                

        def Hit(self):
                Main.play_hit()
                Main.hit_anyone()
                Main.check_blackjack()
                Main.play_round_end()
                        

        def Stand(self):
                Main.hit_anyone()
                Main.check_blackjack()
                Main.play_round_end()
                        
        def NewHand(self):
                Main.play_deal()
                
                

Blackjack()

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

                self.a1=tkinter.Button(window, text="Deal", command=self.Deal)
                self.a2=tkinter.Button(window, text="Hit", command=self.Hit)
                self.a3=tkinter.Button(window, text="Stand", command=self.Stand)
                self.a4=tkinter.Button(window, text="New Hand", command=self.NewHand)
                self.a5=tkinter.Button(window, text="1000", command=lambda:chip_pressed('1000'))
                self.a6=tkinter.Button(window, text="500", command=lambda:chip_pressed('500'))
                self.a7=tkinter.Button(window, text="200", command=lambda:chip_pressed('200'))
                self.a8=tkinter.Label(window, text="Balance :")
                self.a9=tkinter.Button(window, text="New Game", command=self.NewGame)
                self.p1=tkinter.Label(window, text="Dealer", bg="white")
                self.p2=tkinter.Label(window, text="Player1", bg="white")
                self.p3=tkinter.Label(window, text="Player2", bg="white")
                self.l1=tkinter.Button(window, text="Easy", command=self.Easy)
                self.l2=tkinter.Button(window, text="Normal", command=self.Normal)
                self.l3=tkinter.Button(window, text="Hard", command=self.Hard)


                self.a1.place(x=150, y=300, width=90, height=50)
                self.a2.place(x=300, y=300, width=90, height=50)
                self.a3.place(x=450, y=300, width=90, height=50)
                self.a4.place(x=20, y=30, width=80, height=40)
                self.a5.place(x=20, y=90, width=50, height=50)
                self.a6.place(x=20, y=150, width=50, height=50)
                self.a7.place(x=20, y=210, width=50, height=50)
                self.a8.place(x=20, y=320, width=50, height=30)
                self.a9.place(x=20, y=10, width=80, height=30)
                self.p1.place(x=300, y=25, width=70, height=30)
                self.p2.place(x=120, y=150, width=70, height=30)
                self.p3.place(x=500, y=150, width=70, height=30)
                self.l1.place(x=400, y=10, width=70, height=30)
                self.l2.place(x=480, y=10, width=70, height=30)
                self.l3.place(x=560, y=10, width=70, height=30)

                def chip_pressed(value):
    
                    num_entry.insert("end", value)  
                    print(value,"pressed")


                entry_value=tkinter.StringVar(window, value='')

                num_entry=tkinter.Entry(window, textvariable=entry_value, width=10)
                num_entry.grid(row=0, columnspan=1)
                num_entry.place(x=20, y=290)
     
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
                
                main.set_level("easy")
                self.Playing()

        def Normal(self):

                main.set_level("normal")
                self.Playing()

        def Hard(self):

                main.set_level("hard")
                self.Playing()

                

        def Playing(self):
                main.user_betting(chip)
                main.calculate_chip()
                main.play_start()
                main.make_players(name1, name2)

                def Deal(self):
                        self.hit.configure(state='normal')
                        self.stand.configure(state='normal')

                        self.dealer=self.deck.deal(2)
                        self.player1=self.deck.deal(2)
                        self.player2=self.deck.deal(2)
                        self.user=self.deck.deal(2)

                        self._dealercard[0].display('front', self.dealer[0]._id)
                        self._dealercard[1].display('back', self.dealer[1]._id)

                        self._player1card[0].display('front', self.dealer[0]._id)
                        self._player1card[1].display('back', self.dealer[1]._id)

                        self._player2card[0].display('front', self.dealer[0]._id)
                        self._player2card[1].display('back', self.dealer[1]._id)

                        self._usercard[0].display('front', self.dealer[0]._id)
                        self._usercard[1].display('back', self.dealer[1]._id)

                        main.play_deal()
                
                        main.play_continue()

                def Hit(self):
                        main.play_hit()
                        main.hit_anyone()
                        main.check_blackjack()
                        main.play_round_end()
                        

                def Stand(self):
                        main.hit_anyone()
                        main.check_blackjack()
                        main.play_round_end()
                        
                def NewGame(self):
                        main.play_game_end()

                def NewHand(self):
                        main.play_start()
                
                
                
                
                
 if __name__=="__main__":
         Blackjack()
                
                
