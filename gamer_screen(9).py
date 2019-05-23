import tkinter
from tkinter import Image
import Dealer
from User import User
from CountingPlayer import CountingPlayer
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

                self.a1=tkinter.Button(self.window, text="Deal", command=self.Button_Deal)
                self.a2=tkinter.Button(self.window, text="Hit", command=self.Hit)
                self.a3=tkinter.Button(self.window, text="Stand", command=self.Stand)
                self.a4=tkinter.Button(self.window, text="Clear", command=self.Clear)
                self.a5=tkinter.Button(self.window, text="1000", command=lambda:chip_pressed('1000'))
                self.a6=tkinter.Button(self.window, text="500", command=lambda:chip_pressed('500'))
                self.a7=tkinter.Button(self.window, text="200", command=lambda:chip_pressed('200'))
                self.a8=tkinter.Label(self.window, text="Balance :")
                self.a9=tkinter.Label(self.window, text="New Game :")
                self.p1=tkinter.Label(self.window, text="Dealer", bg="white")
                self.p2=tkinter.Label(self.window, text="Player1", bg="white")
                self.p3=tkinter.Label(self.window, text="Player2", bg="white")
                self.l1=tkinter.Button(self.window, text="Easy", command=self.Easy)
                self.l2=tkinter.Button(self.window, text="Normal", command=self.Normal)
                self.l3=tkinter.Button(self.window, text="Hard", command=self.Hard)


                self.a1.place(x=150, y=330, width=90, height=45)
                self.a2.place(x=300, y=330, width=90, height=45)
                self.a3.place(x=450, y=330, width=90, height=45)
                self.a4.place(x=20, y=10, width=80, height=30)
                self.a5.place(x=20, y=90, width=50, height=50)
                self.a6.place(x=20, y=150, width=50, height=50)
                self.a7.place(x=20, y=210, width=50, height=50)
                self.a8.place(x=20, y=320, width=50, height=30)
                self.a9.place(x=300, y=10, width=70, height=30)
                self.p1.place(x=300, y=150, width=70, height=30)
                self.p2.place(x=120, y=250, width=70, height=30)
                self.p3.place(x=500, y=250, width=70, height=30)
                self.l1.place(x=380, y=10, width=70, height=30)
                self.l2.place(x=460, y=10, width=70, height=30)
                self.l3.place(x=540, y=10, width=70, height=30)

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
                    return value
                    # print(int(num_entry.get()))


                entry_value=tkinter.StringVar(self.window, value='')

                num_entry=tkinter.Entry(self.window, textvariable=entry_value, width=10)
                num_entry.grid(row=0, columnspan=1)
                num_entry.place(x=20, y=290)
                
                image_directory='./cardimages/'
                
                self.window.mainloop()

     
        def set_level(my_level) :
                
                if my_level == "easy" :
                        make_players("Hi-Lo", "KO")
                elif my_level == "normal" :
                        make_players("Hi-Opt2", "Zen")
                elif my_level == "hard" :
                        make_players("Halves", "Hi-Opt2")


        def make_players(name1, name2) :
                

    # player_list[0] = 카운팅 플레이어1
    # player_list[1] = 유저
    # player_list[2] = 카운팅 플레이어2
    # 항상 고정
                player_list.append(CountingPlayer.CountingPlayer(name1))
                player_list.append(User.User())
                player_list.append(CountingPlayer.CountingPlayer(name2))

                

        def play_new_game(my_level):
                Dealer.dealer.HANDLER.reset()
                self.set_level(my_level)

                dealer.new_game()
                for i in range(len(player_list)) :
                        
                        player_list[i].new_game()

                play_start()
                


        def Easy(self):
                
               self.play_new_game("easy")
                

        def Normal(self):

                self.play_new_game("easy")


        def Hard(self):

                Main.set_level("hard")


        def give_my_card_info(num, card) :
                

            # 유저와 자기 자신은 포함하지 않기 위해 사용하는 if문
            for i in range(len(player_list)) :
                if i != 1 and i!= num:
                    player_list[i].others_card(card)

            return card       

        def Playing(self):
                
                Main.play_start()


        def Change_to_image(card):
               for i in range(52):
                       if card[0]==deck[i][0] and card[1]==deck[i][1]:
                               _id=deck[i][4]
                               return _id

        def Button_Deal(self):
                

                self.a5.config(state="disabled")
                self.a6.config(state="disabled")
                self.a7.config(state="disabled")

                #user_chips=self.chip_pressed(value)
                #Main.user_betting(user_chips)
                #Main.calculate_chip()

                #user_balance=10000-user_chips

                #result_value=tkinter.StringVar(self.window, value='')

                #user_balance=tkinter.Entry(self.window, textvariable=entry_value, width=10)
                #user_balance.grid(row=0, columnspan=1)
                #user_balance.place(x=70, y=350)


                # deck에 8장 이하만 남으면 덱을 초기화
                if Dealer.Dealer.HANDLER.get_remaining_card() <= 0.5 :
                        
                        
                        dealer.HANDLER.reset()        

            #hit 가능한 상태로 초기화
                Dealer.Dealer.play_status = "st_hit"
                
                        
                for i in range(len(player_list)) :
                        if player_list[i].has_money() :
                                
                                
                                 player_list[i].play_status = "st_hit"

            # deal
                dealer.deal()
                for i in range (len(player_list)) :
                        
                        if player_list[i].is_playable() :
                            player_list[i].deal()

            # dealer.open_deal_card()
                a = self.give_my_card_info(3,dealer.hand[0])
                dealer_cards=tkinter.PhotoImage(file=Blackjack.image_directory+"card{}.gif".format(Chage_to_image(a)))
                lb_d_c=tkinter.Label(window, image=deale_cards)
                lb_d_c.place(x=200, y=50)

            
                for i in range (len(player_list)) :
                
                # 카드를 받았으면 (이 부분 수정해야되나?)
                        if player_list[i].hand :
                                                b=give_my_card_info(i, player_list[0].hand[0])
                                                player1_1=tkinter.PhotoImage(file=Blackjack.image_directory+"card{}.gif".format(Change_to_image(b)))
                                                lb_p1_1=tkinter.Label(window, image=player1_1)
                                                lb_p1_1.place(x=150, y=100)

                                                c=give_my_card_info(i, player_list[0].hand[1])
                                                player1_2=tkinter.PhotoImage(file=Blackjack.image_directory+"card{}.gif".format(Change_to_image(c)))
                                                lb_p1_2=tkinter.Label(window, image=player1_2)
                                                lb_p1_2.place(x=180, y=100)

                                                d=give_my_card_info(i, player_list[1].hand[0])
                                                player2_1=tkinter.PhotoImage(file=Blackjack.image_directory+"card{}.gif".format(Change_to_image(d)))
                                                lb_p2_1=tkinter.Label(window, image=player2_1)
                                                lb_p2_1.place(x=300, y=250)

                                                e=give_my_card_info(1,Main.player_list[1].hand[1])
                                                player2_2=tkinter.PhotoImage(file=Blackjack.image_directory+"card{}.gif".format(Change_to_image(e)))
                                                lb_p2_2=tkinter.Label(window, image=player2_2)
                                                lb_p2_2.place(x=330, y=250)

                                                f=give_my_card_info(1,Main.player_list[2].hand[0])
                                                player3_1=tkinter.PhotoImage(file=Blackjack.image_directory+"card{}.gif".format(Change_to_image(f)))
                                                lb_p3_1=tkinter.Label(window, image=player3_1)
                                                lb_p3_1.place(x=450, y=100)

                                                g=give_my_card_info(1,Main.player_list[2].hand[1])
                                                player3_2=tkinter.PhotoImage(file=Blackjack.image_directory+"card{}.gif".format(Change_to_image(g)))
                                                lb_p3_2=tkinter.Label(window, image=player3_2)
                                                lb_p3_2.place(x=480, y=100)

                                                
                                
                
                current_information()
                play_continue()


             
        def Hit(self):
                
                Main.choice="hit"
                Main.play_hit()
                

                        

        def Stand(self):

                Main.choice="stand"
                Main.play_hit()


        def Clear(self):
                self.a5.config(state="normal")
                self.a6.config(state="normal")
                self.a7.config(state="normal")
                

dealer = Dealer.Dealer()
player_list = []
winner_list = []
                
                

Blackjack()
