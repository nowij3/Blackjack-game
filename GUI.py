# -*- coding: utf-8 -*-
import tkinter
from tkinter import Image
from tkinter import messagebox
from Deck import Deck
import Dealer
import User
import CountingPlayer
import time

#######
# GUI #
#######

# GUI 화면 보여주기
def show_panel(window) :

    window.title("BlackJack Game")
    window.geometry("650x500+100+100")
    window.resizable(True, True)

    entry_value=tkinter.StringVar(window, value='')

    num_entry=tkinter.Entry(window, textvariable=entry_value, width=8)
    num_entry.grid(row=0, columnspan=1)
    num_entry.place(x=20, y=340)


    a5=tkinter.Button(window, text="1000", command=lambda:chip_pressed(num_entry,'1000', a1))
    a6=tkinter.Button(window, text="500", command=lambda:chip_pressed(num_entry,'500', a1))
    a7=tkinter.Button(window, text="200", command=lambda:chip_pressed(num_entry,'200', a1))
    a4=tkinter.Button(window, text="Clear", command=lambda:button_clear(num_entry, a1, a5, a6, a7))
    h1=tkinter.Button(window, text="Help", command=lambda:msghelp())


    a8=tkinter.Label(window, text="Balance : 1000000")
    b1=tkinter.Label(window, text="Balance : 1000000")
    b2=tkinter.Label(window, text="Balance : 1000000")###Balance 창에 표시
    
    a1=tkinter.Button(window, text="Deal", command=lambda:button_deal(num_entry, a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, window))
    a2=tkinter.Button(window, text="Hit", command=lambda:button_hit(a2))
    a3=tkinter.Button(window, text="Stand", command=lambda:button_stand(a2, a3, a4, a5, a6, a7, num_entry,a8,b1,b2))
        

    
    a9=tkinter.Label(window, text="New Game :")
    p1=tkinter.Label(window, text="Dealer", bg="white")
    p2=tkinter.Label(window, text="Player1", bg="white")
    p3=tkinter.Label(window, text="Player2", bg="white")
    l1=tkinter.Button(window, text="Easy", command=lambda:button_easy(a2, a3, a4,a5,a6,a7,p2,p3,a8,b1,b2,num_entry))
    l2=tkinter.Button(window, text="Normal", command=lambda:button_normal(a2, a3, a4,a5,a6,a7,p2,p3,a8,b1,b2,num_entry))
    l3=tkinter.Button(window, text="Hard", command=lambda:button_hard(a2, a3, a4,a5,a6,a7,p2,p3,a8,b1,b2,num_entry))
    
    a1.place(x=150, y=430, width=90, height=45)
    a2.place(x=300, y=430, width=90, height=45)
    a3.place(x=450, y=430, width=90, height=45)
    a4.place(x=20, y=10, width=80, height=30)
    a5.place(x=20, y=140, width=50, height=50)
    a6.place(x=20, y=200, width=50, height=50)
    a7.place(x=20, y=260, width=50, height=50)
    a8.place(x=14, y=370, width=110, height=30)
    b1.place(x=120, y=300, width=110, height=30)
    b2.place(x=500, y=300, width=110, height=30)
    a9.place(x=300, y=10, width=70, height=30)
    p1.place(x=300, y=150, width=70, height=30)
    p2.place(x=120, y=270, width=70, height=30)
    p3.place(x=500, y=270, width=70, height=30)
    l1.place(x=380, y=10, width=70, height=30)
    l2.place(x=460, y=10, width=70, height=30)
    l3.place(x=540, y=10, width=70, height=30)
    h1.place(x=110, y=10, width=80, height=30)

    a1.config(state='disabled')
    a2.config(state='disabled')
    a3.config(state='disabled')
    a4.config(state='disabled')
    a5.config(state='disabled')
    a6.config(state='disabled')
    a7.config(state='disabled')
    
    image_directory='./cardimages/'
    

def chip_pressed(num_entry, value, a1):
    a1.config(state='normal')
    
    if not num_entry.get() == '':
        v = int(value)
        v += int(num_entry.get())

        num_entry.delete(0,'end')
        num_entry.insert("end", str(v))

    else:
        num_entry.insert("end", value)

    print(value,"pressed")
    player_list[1].chip_choice+=int(value)
    return value

def msghelp():
    tkinter.messagebox.showinfo("How To Play Game", "블랙잭 게임은 카드를 뽑아 숫자의 합이 21을 넘지 않으면서 21에 가까운 사람이 승리합니다.\n21을 초과하는 것을 Bust라고 하며 게임에서 패배를 의미합니다.\nA는 1 또는 11, J, Q, K는 각 10으로 계산합니다.\n게임을 시작하려면 우측 상단의 난이도를 선택해야합니다.\n각 난이도에 참여하는 플레이어는 다음과 같습니다.\nEasy - Hi-Opt2, Zen  |  Normal - Halves, Hi-Lo  |  Hard - Hi-Lo, KO\n각 칩 버튼을 눌러 베팅 금액을 조절할 수 있습니다.\nClear 버튼을 눌러서 베팅 금액을 초기화할 수 있습니다.\n베팅 금액을 결정했다면 Deal을 눌러야 게임이 시작됩니다.\nDeal은 게임을 처음 시작할 때 2장의 카드를 받는 것을 말합니다.\n이때 카드 2장으로 21을 만드는 경우를 블랙잭이라고 하며, 베팅 금액의 2.5배를 받게 됩니다.\n플레이어가 받은 카드는 모두 공개하며, 딜러는 처음 받은 카드 두 장 중에서 한 장만 공개합니다.\nDeal 이후 플레이어는 Hit을 할지, Stand를 할지 선택합니다.\nHit은 카드를 한 장 더 받는 것을 말합니다.\nBust가 되기 전까지 횟수 제한은 없습니다.\nStand는 카드를 더 이상 받지 않는 것을 말합니다.\n블랙잭이 아니면서 Bust가 되지 않은 플레이어는 딜러보다 카드 합이 클 때만 배팅 금액의 2배를 받게 됩니다.\nBust가 되지 않으면서 딜러와 비긴 경우 베팅 금액을 돌려받습니다.")       

    
def button_clear(num_entry, a1, a5, a6, a7):

    num_entry.delete(0,'end')
    a1.config(state='disabled')


def button_easy(a2, a3, a4,a5,a6,a7,p2,p3,a8,b1,b2,num_entry):
    a4.config(state="normal")
    a5.config(state="normal")
    a6.config(state="normal")
    a7.config(state="normal")
    easy_p2="Hi-Opt2"
    p2.config(text=easy_p2)
    easy_p3="Zen"
    p3.config(text=easy_p3)
    num_entry.config(state='normal')
    num_entry.delete(first=0, last=100)
    remove_card()
    play_new_game("easy",a2, a3, a4, a5, a6, a7,a8,b1,b2)
                
def button_normal(a2, a3, a4,a5,a6,a7,p2,p3,a8,b1,b2,num_entry):
    a4.config(state="normal")
    a5.config(state="normal")
    a6.config(state="normal")
    a7.config(state="normal")
    easy_p2="Halves"
    p2.config(text=easy_p2)
    easy_p3="Halves"
    p3.config(text=easy_p3)
    num_entry.config(state='normal')
    num_entry.delete(first=0, last=100)
    remove_card()
    play_new_game("normal",a2, a3, a4, a5, a6, a7,a8,b1,b2)
    
def button_hard(a2, a3, a4,a5,a6,a7,p2,p3,a8,b1,b2,num_entry):
    a4.config(state="normal")
    a5.config(state="normal")
    a6.config(state="normal")
    a7.config(state="normal")
    easy_p2="KO"
    p2.config(text=easy_p2)
    easy_p3="Hi-Lo"
    p3.config(text=easy_p3)
    num_entry.config(state='normal')
    num_entry.delete(first=0, last=100)
    remove_card()
    play_new_game("hard",a2, a3, a4, a5, a6, a7,a8,b1,b2)

def change_to_image(card):
    for i in range(52):
        if card[0]==Deck.deck[i][0] and card[1]==Deck.deck[i][1]:
            _id=Deck.deck[i][4]
            
            file_name = "./cardimages/card" + str(_id) + ".gif"
            return file_name
        
def button_deal(num_entry, a1, a2, a3, a4, a5, a6, a7, a8, b1,b2,window):

    global num_of_hit
    num_of_hit = 0

    # 베팅칩 못누르게
    a2.config(state="normal")
    a3.config(state="normal")
    a4.config(state="disabled")
    a5.config(state="disabled")
    a6.config(state="disabled")
    a7.config(state="disabled")

    num_entry.config(state='readonly')
    

    tmp = "Balance : " + str(player_list[1].balance - player_list[1].chip_choice)
    a8.config(text = tmp)

    tmp_1 = "Balance : " + str(player_list[0].balance - player_list[0].chip_choice)
    b1.config(text = tmp_1)

    tmp_2 = "Balance : " + str(player_list[2].balance - player_list[2].chip_choice)
    b2.config(text = tmp_2)
    # 유저 chip_choice 변수에 베팅칩 반영
    #player_list[1].chip_choice = num_entry

    # deck에 8장 이하만 남으면 덱을 초기화
    # 카운팅 플레이어의 카운팅 초기화
    if dealer.HANDLER.get_remaining_card() <= 0.5 :
            dealer.HANDLER.reset()

    for i in range(len(player_list)) :
        if i != 1 :
            player_list[i].counting = 0       

    # hit 가능한 상태로 초기화
    dealer.play_status = "st_hit"
    for i in range(len(player_list)) :
        if player_list[i].has_money() :
             player_list[i].play_status = "st_hit"

    # deal
    dealer.deal()
    for i in range (len(player_list)) :
        if player_list[i].is_playable() :
            player_list[i].deal()

    give_my_card_info(len(player_list)+1,dealer.hand[0])
    card=tkinter.PhotoImage(file=change_to_image(dealer.hand[0]))

    lb_d_c=tkinter.Label(window, image=card)
    lb_d_c.place(x=220, y=40)
    
    d_cards.append(lb_d_c)
    card_labels.append(lb_d_c) #@

    for i in range (len(player_list)) :
        if player_list[i].hand :
            give_my_card_info(i, player_list[0].hand[0])
            player1_1=tkinter.PhotoImage(file=change_to_image(player_list[0].hand[0]))
            lb_p1_1=tkinter.Label(window, image=player1_1)
            lb_p1_1.place(x=100, y=150)

            card_labels.append(lb_p1_1) #@

            give_my_card_info(i, player_list[0].hand[1])
            player1_2=tkinter.PhotoImage(file=change_to_image(player_list[0].hand[1]))
            lb_p1_2=tkinter.Label(window, image=player1_2)
            lb_p1_2.place(x=130, y=150)

            card_labels.append(lb_p1_2) #@

            give_my_card_info(i, player_list[1].hand[0])
            player2_1=tkinter.PhotoImage(file=change_to_image(player_list[1].hand[0]))
            lb_p2_1=tkinter.Label(window, image=player2_1)
            lb_p2_1.place(x=240, y=320)

            card_labels.append(lb_p2_1) #@

            give_my_card_info(i, player_list[1].hand[1])
            player2_2=tkinter.PhotoImage(file=change_to_image(player_list[1].hand[1]))
            lb_p2_2=tkinter.Label(window, image=player2_2)
            lb_p2_2.place(x=270, y=320)

            card_labels.append(lb_p2_2) #@

            give_my_card_info(i, player_list[2].hand[0])
            player3_1=tkinter.PhotoImage(file=change_to_image(player_list[2].hand[0]))
            lb_p3_1=tkinter.Label(window, image=player3_1)
            lb_p3_1.place(x=420, y=150)

            card_labels.append(lb_p3_1) #@

            give_my_card_info(i, player_list[2].hand[1])
            player3_2=tkinter.PhotoImage(file=change_to_image(player_list[2].hand[1]))
            lb_p3_2=tkinter.Label(window, image=player3_2)
            lb_p3_2.place(x=450, y=150)

            card_labels.append(lb_p3_2) #@

    if player_list[1].hand_sum == 21 :
        a2.config(state='disabled')
        ### disable hit button
    a1.config(state="disabled")
    window.mainloop()

    
def button_hit(a2):
    
    global num_of_hit
    
    if player_list[1].hand_sum == 21 :
        a2.config(state='disabled')


    if player_list[1].is_playable():
        player_list[1].hit()
        give_my_card_info(1, player_list[1].hand[-1])
        uc=tkinter.PhotoImage(file=change_to_image(player_list[1].hand[-1]))
        uc_1=tkinter.Label(window, image=uc)
        uc_1.place(x=300+(num_of_hit*30), y=320)
        card_labels.append(uc_1)#@
        print(num_of_hit)


    #if num_of_hit==1:
        #if player_list[1].is_playable() :
            #player_list[1].hit()
            #give_my_card_info(1, player_list[1].hand[-1])
            #uc2=tkinter.PhotoImage(file=change_to_image(player_list[1].hand[-1]))
            #uc_2=tkinter.Label(window, image=uc2)
            #uc_2.place(x=330, y=220)
            #card_labels.append(uc_2)#@

    #if num_of_hit==2:
        #if player_list[1].is_playable() :
            #player_list[1].hit()
            #give_my_card_info(1, player_list[1].hand[-1])
            #uc3=tkinter.PhotoImage(file=change_to_image(player_list[1].hand[-1]))
            #uc_3=tkinter.Label(window, image=uc3)
            #uc_3.place(x=360, y=220)
            #card_labels.append(uc_3)#@
            

    if (player_list[1].hand_sum > 21) :
        
        player_list[1].play_status = "st_bust"
        a2.config(state='disabled')

    num_of_hit += 1
            
    window.mainloop()


def button_stand(a2, a3, a4, a5, a6, a7, num_entry,a8,b1,b2):

    a3.config(state='disabled')
    if player_list[1].is_playable() :
        player_list[1].play_status = "st_stand"
    play_hit(a2, a3, a4, a5, a6, a7, num_entry,a8,b1,b2)
   

    window.mainloop()
    
def add_card(card):
    cards.append(card)


######################
# 게임 진행 관련함수 #
######################

# 유저가 베팅할 칩 선택 (GUI로 인풋받기)
def user_betting(chip) :
    chip=chip_pressed(num_entry, value, a1)
    player_list[1].chip_choice = chip

def reset_betting():
    player_list[1].chip_choice = 0

# 블랙잭인 경우 베팅한 금액의 2.5배, 그 외엔 2배 반환
def prize_chip(player) :

    # 딜러와 비긴 경우
    if player.hand_sum == dealer.hand_sum :
        ##print(player.name, "recieves ", player.chip_choice)
        return player.chip_choice

    if player.is_blackjack() :
        ##print(player.name, "recieves ", int(2.5 * player.chip_choice))
        return int(2.5 * player.chip_choice)
    else :
        ##print(player.name, "recieves ", 2 * player.chip_choice)
        return 2 * player.chip_choice


# 재산에 상금 반영하기
def get_prize() :

    info = ""

    for i in range(len(player_list)) :
        # 게임에 참여한 경우에만
        if player_list[i].has_money() :
            player_list[i].balance -= player_list[i].chip_choice

    # 블랙잭 우승자
    for i in range(len(blackjack_winner_list)) :
        if blackjack_winner_list[i].name == 'Dealer' :
            break
        else :
            blackjack_winner_list[i].balance += prize_chip(blackjack_winner_list[i])
            info += blackjack_winner_list[i].name + " recives " + str(prize_chip(blackjack_winner_list[i])) + "\n"

    # 블랙잭이 아닌 우승자
    for i in range(len(winner_list)) :
        if winner_list[i].name == 'Dealer' :
            continue
        elif dealer.is_bust() :
            winner_list[i].balance += prize_chip(winner_list[i])
            info += winner_list[i].name + " recives " + str(prize_chip(winner_list[i])) + "\n"
            
        else :
            winner_list[i].balance += prize_chip(winner_list[i])
            info += winner_list[i].name + " recives " + str(prize_chip(winner_list[i])) + "\n"

    # 비긴 플레이어
    for i in range(len(draw_list)) :
        draw_list[i].balance += prize_chip(draw_list[i])
        info += draw_list[i].name + " recives " + str(prize_chip(draw_list[i])) + "\n"

    if info == "" :
        info += "Round end!"

    messagebox.showinfo("Info", info)


# hit 상태인 플레이어가 남아있는지 확인
def hit_anyone() :

    for i in range(len(player_list)) :
        if player_list[i].is_playable() :
            return True

    # 아무도 hit하지 않으면
    return False

# 모든 플레이어가 파산 상태인지 확인
def check_all_money_status() :

    for i in range(len(player_list)) :
        if player_list[i].has_money() :
            return True

    # 모두가 파산이면
    return False

# 난이도 설정
def set_level(my_level) :


    if my_level == "easy" :
        make_players("Hi-Opt2", "Zen")
    elif my_level == "normal" :
        make_players("Halves", "Hi-Lo")
    elif my_level == "hard" :
        make_players("KO", "Hi-Lo")

# 게임에 참여하는 플레이어 생성
def make_players(name1, name2) :

    # 플레이어 리스트 초기화
    del player_list[:]
    
    # player_list[0] = 카운팅 플레이어1
    # player_list[1] = 유저
    # player_list[2] = 카운팅 플레이어2
    # 항상 고정
    player_list.append(CountingPlayer.CountingPlayer(name1))
    player_list.append(User.User())
    player_list.append(CountingPlayer.CountingPlayer(name2))


# 플레이어 중 블랙잭이 있는지 확인
def check_blackjack() :

    # 딜러 제외 플레이어 중 블랙잭이 있는지 확인
    for i in range(len(player_list)) :
        if player_list[i].is_blackjack() :
            blackjack_winner_list.append(player_list[i])

    # 블랙잭인 플레이어가 없을 때 딜러가 블랙잭인지 확인
    if not blackjack_winner_list and dealer.is_blackjack() :
        blackjack_winner_list.append(dealer)


# 아무도 블랙잭이 아닌 경우 21에 가장 가까운 플레이어(우승자) 찾기
def find_winner() :

    # 블랙잭 우승자 찾기
    check_blackjack()

    for i in range(len(player_list)) :
        # 게임에 참여한 플레이어만
        if player_list[i].has_money() :

            # 블랙잭이 아닌 플레이어만 확인
            if not player_list[i].is_blackjack() :

                # 플레이어가 파산이면 딜러 우승
                if player_list[i].is_bust() :
                    if not dealer.is_bust() :
                        winner_list.append(dealer)
                    # 둘 다 파산인 경우
                    else :
                        continue                        

                # 딜러만 파산인 경우
                elif dealer.is_bust() :
                    winner_list.append(player_list[i])
                                       
                # 딜러와 플레이어 둘 다 파산이 아닐 때
                else :

                    # 플레이어의 카드 값이 딜러보다 높은 경우
                    if player_list[i].hand_sum > dealer.hand_sum :
                        winner_list.append(player_list[i])

                    # 비긴 경우
                    elif player_list[i].hand_sum == dealer.hand_sum :
                        draw_list.append(player_list[i])

                
# 다른 플레이어에게 내 카드 정보 주기, CountingPlayer들만 적용됨
def give_my_card_info(num, card) :

    # 유저와 자기 자신은 포함하지 않기 위해 사용하는 if문
    # 유저는 player_list[1]
    for i in range(len(player_list)) :
        if i != 1 and i!= num:
            player_list[i].others_card(card)

# 게임 시작, 모두 초기화
def play_new_game(choice, a2, a3, a4, a5, a6, a7,a8,b1,b2) :

    dealer.HANDLER.reset()

    set_level(choice)


    dealer.new_game()
    for i in range(len(player_list)) :
        player_list[i].new_game()

    play_start(a2, a3, a4, a5, a6, a7,a8,b1,b2)

# 게임 시작, 베팅칩만 초기화
def play_new_hand(a2, a3, a4, a5, a6, a7, num_entry,a8,b1,b2) :

    print("\n***NEW HAND START***")

    dealer.new_hand()

    for i in range(len(player_list)) :
        if player_list[i].has_money :
            player_list[i].new_hand()

    ### 라벨 지우기 tkinter.Label.destroy()?
    num_entry.config(state='normal')
    num_entry.delete(first=0, last=100)
    remove_card()
    reset_betting()
    


    play_start(a2, a3, a4, a5, a6, a7,a8,b1,b2)

# 라운드 시작
def play_start(a2, a3, a4, a5, a6, a7,a8,b1,b2) :

    # 우승자 리스트 비우기
    del blackjack_winner_list[:]
    del winner_list[:]
    del draw_list[:]

    a2.config(state="disabled")
    a3.config(state="disabled")

    print(" ")
    # 각자의 재산 출력
    for i in range(len(player_list)) :
        print("current balance of ",player_list[i].name, ": ", player_list[i].balance)

    tmp = "Balance : " + str(player_list[1].balance)
    a8.config(text = tmp)
    tmp_1 = "Balance : " + str(player_list[0].balance)
    b1.config(text = tmp_1)
    tmp_2 = "Balance : " + str(player_list[2].balance)
    b2.config(text = tmp_2)

    print(" ")
    for i in range(len(player_list)) :
        #유저 제외한 플레이어들에게 베팅칩 입력받기
        if i != 1 :
            player_list[i].decide_betting()
            print("betting chip of ",player_list[i].name," : ", player_list[i].chip_choice)

    a4.config(state="normal")
    a5.config(state="normal")
    a6.config(state="normal")
    a7.config(state="normal")
    ### 칩 버튼 enable

# 딜
def play_deal() :

    # deck에 8장 이하만 남으면 덱을 초기화
    # 카운팅 플레이어의 카운팅 초기화
    if dealer.HANDLER.get_remaining_card() <= 0.5 :
        dealer.HANDLER.reset()
        for i in range(len(player_list)) :
            if i != 1 :
                player_list[i].counting = 0

    # hit 가능한 상태로 초기화
    dealer.play_status = "st_hit"
    for i in range(len(player_list)) :
        if player_list[i].has_money() :
            player_list[i].play_status = "st_hit"

    # deal
    dealer.deal()
    for i in range (len(player_list)) :
        if player_list[i].is_playable() :
            player_list[i].deal()

    # dealer.open_deal_card()
    give_my_card_info(len(player_list)+1, dealer.hand[0])

    for i in range (len(player_list)) :
        # 카드를 받았으면
        if player_list[i].hand :
            # 첫 두 장 정보 주기
            give_my_card_info(i, player_list[i].hand[0])
            give_my_card_info(i, player_list[i].hand[1])

    current_information()
    window.mainloop()

# 히트 이후 게임 진행
def play_continue(a2, a3, a4, a5, a6, a7, num_entry,a8,b1,b2) :

    # 모두의 hit가 끝나면
    # 딜러의 딜에서 받은 뒤집히지 않은 카드 오픈
    dealer.open_second_card()
    give_my_card_info(len(player_list)+1, dealer.hand[1])
    card_2=tkinter.PhotoImage(file=change_to_image(dealer.hand[1]))
    lb_d_c2=tkinter.Label(window, image=card_2)
    lb_d_c2.place(x=250, y=40)
    ### 카드 이미지 !변경!

    # 딜러가 카드를 hit 할 때 마다 다른 플레이어들에게 카드 정보 주기
    i = 0
    while dealer.make_decision() :
        give_my_card_info(len(player_list)+1, dealer.hand[-1])
        card_3=tkinter.PhotoImage(file=change_to_image(dealer.hand[-1]))
        d_cards.append(card_3)
        lb_d_c3=tkinter.Label(window, image=card_3)
        lb_d_c3.place(x=280+(i*30), y=40)
        i+=1
        card_labels.append(lb_d_c3)
        ### 카드 이미지

    final_information()
    play_round_end(a2, a3, a4, a5, a6, a7, num_entry,a8,b1,b2)


# 히트
def play_hit(a2, a3, a4, a5, a6, a7, num_entry,a8,b1,b2) :

    i=0
    while player_list[0].is_playable() :
        # hit 한 경우에만 카드 정보 나눠주기
        if player_list[0].make_decision(dealer.hand[0]) :
            give_my_card_info(0, player_list[0].hand[-1])
            p_0_img = tkinter.PhotoImage(file=change_to_image(player_list[0].hand[-1]))
            p0_cards.append(p_0_img)
            p_0_lbl = tkinter.Label(window, image=p_0_img)
            p_0_lbl.place(x=160+(i*30), y=150)
            i+=1
            card_labels.append(p_0_lbl)
            ### GUI 카드 이미지

    j=0
    while player_list[2].is_playable() :
        if player_list[2].make_decision(dealer.hand[0]) :
            give_my_card_info(2, player_list[2].hand[-1])
            player3_3=tkinter.PhotoImage(file=change_to_image(player_list[2].hand[-1]))
            p2_cards.append(player3_3)
            p3_3=tkinter.Label(window, image=player3_3)
            p3_3.place(x=480+(j*30), y=150)
            j+=1
            card_labels.append(p3_3)
            ### GUI 카드 이미지

    play_continue(a2, a3, a4, a5, a6, a7, num_entry,a8,b1,b2)


# 한 라운드 종료
def play_round_end(a2, a3, a4, a5, a6, a7, num_entry,a8,b1,b2) :

    print("\n***ROUND END***\n")

    ### 우승자 찾기
    find_winner()

    ### 상금 받기
    get_prize()

    # 모두가 파산이면
    if not check_all_money_status() :
        ###라벨지우기
        play_game_end()
    else :
        play_new_hand(a2, a3, a4, a5, a6, a7, num_entry,a8,b1,b2)


# 메인 게임 종료
def play_game_end() :

    # GUI에서 new game 제외한 모든 버튼 선택 못 하게 구현 필요
    print("***GAME END***")

# 메인 테스트 함수, 딜러가 카드 한 장만 오픈했을 때
def current_information() :

    print("\ncurrent information")

    print(dealer.name, " : ", dealer.hand[0] , ", hand_num : ", dealer.hand_num, ", hand_sum : ", dealer.hand_sum)

    for i in range(len(player_list)) :

        # 게임에 참여했다면
        if player_list[i].has_money() :
            # 유저의 경우
            if i == 1 :
                print(player_list[1].name," : ",player_list[1].hand, ", hand_num : ", player_list[1].hand_num, "hand_sum : ", player_list[1].hand_sum, ", play_status : ", player_list[1].play_status)
            else :
                print(player_list[i].name," : ",player_list[i].hand, ", hand_num : ", player_list[i].hand_num, ", hand_sum : ", player_list[i].hand_sum, ", counting : ", player_list[i].counting, ", play_status : ", player_list[i].play_status)

# 메인 테스트 함수
def final_information() :

    print("\nfinal information")

    print(dealer.name, " : ", dealer.hand , ", hand_num : ", dealer.hand_num, ", hand_sum : ", dealer.hand_sum, ", play_status : ", dealer.play_status)

    for i in range(len(player_list)) :

        # 게임에 참여했다면
        if player_list[i].has_money() :
            # 유저의 경우
            if i == 1 :
                print(player_list[1].name," : ",player_list[1].hand, ", hand_num : ", player_list[1].hand_num, "hand_sum : ", player_list[1].hand_sum, ", play_status : ", player_list[1].play_status)
            else :
                print(player_list[i].name," : ",player_list[i].hand, ", hand_num : ", player_list[i].hand_num, ", hand_sum : ", player_list[i].hand_sum, ", counting : ", player_list[i].counting, ", play_status : ", player_list[i].play_status)
        else :
            print(player_list[i].name," : stop")

def remove_card():
    for label in card_labels:
        label.destroy()


########
# Main #
########

dealer = Dealer.Dealer()
player_list = []
blackjack_winner_list = []
winner_list = []
draw_list = []

d_cards = []
p0_cards = []
p2_cards = []
card_labels = []

num_of_hit = 0

window=tkinter.Tk()
show_panel(window)
window.mainloop()
