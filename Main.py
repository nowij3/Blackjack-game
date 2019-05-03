# -*- coding: utf-8 -*-

import Deck as deck
import Dealer
import CountingPlayer
import User


# 유저가 베팅할 칩 선택 (GUI로 인풋받기)
def user_betting(chip) :
    player_list[1].chip_choice += chip
    player_list[1].balance -= chip_choice


# 모든 플레이어가 베팅한 칩 계산해서 반환
def calculate_chip() :
    
    # user_betting (GUI에서 유저가 칩 선택할 때까지 기다리는 것 구현 필요)
    
    print("called calculate_chip")
    
    total_chip = 0
    for i in range(0, 3) :
        total_chip += player_list[i].chip_choice
    return total_chip


# 블랙잭인 경우 베팅한 금액의 2.5배, 그 외엔 1.5배 반환
def prize_chip(player) :
    if player.blackjack == true :
        return 2.5 * player.chip_choice
    else :
        return 2 * player.chip_choice

    
# 재산에 상금 반영하기
def get_prize(player) :
    player.balance += prize_chip()


# 카드 덱 초기화
def init_deck() :
    deck.reset()

    
# 게임에 참여하는 플레이어 생성
def make_players(name1, name2) :

    print("called make_players")

    # player_list[0] = 카운팅 플레이어1
    # player_list[1] = 유저
    # player_list[2] = 카운팅 플레이어2
    # 항상 고정
    player_list.append(CountingPlayer.CountingPlayer(name1))
    player_list.append(User.User())
    player_list.append(CountingPlayer.CountingPlayer(name2))


# 플레이어 중 블랙잭이 있는지 확인
def check_blackjack() :

    print("called check_blackjack")

    for i in range(0, 3) :
        if player_list[i].is_blackjack() == True :
            winner = player_list[i]
            return True
        
    if dealer.is_blackjack() == True :
        winner = dealer
        return True

    # 아무도 블랙잭이 아니면
    return False


# 다른 플레이어에게 내 카드 정보 주기
def give_my_card_info(i, card) :

    print("called give_my_card_info")

    for j in range(0, 3) :
        if j == i :
            continue
        else :
            # player_list[i]를 제외한 나머지 플레이어들
            player_list[j].others_card(card)
    

# 라운드 시작 (딜)
def play_deal() :
    
    # (GUI에서 deck에 8장 이하만 남으면 덱을 섞기)

    print("called play_deal")

    # hit 가능한 상태로 초기화
    dealer.play_status = "st_hit"
    for i in range(0, 3) :
        player_list[i].play_status = "st_hit"


    # deal
    dealer.deal()
    for i in range (0, 3) :
        player_list[i].deal()

    dealer.open_card()
    for i in range (0, 3) :
        player_list[i].open_deal_card()


# 딜 이후 게임 진행
def play_continue() :

    print("called play_continue")
    
    # 딜 카드에서 블랙잭이 있는 경우
    if check_blackjack() == True :
        play_end()
    else :
        # 딜러의 딜에서 받은 뒤집히지 않은 카드 오픈
        dealer.open_deal_card()
        if check_blackjack == True :
            play_end()

        else :
            for i in range (0, 3) :
                if player_list[i].is_playable == True :
                    my_card = player_list[i].hit()
                    give_mycard_info(i, my_card)
                

# 한 라운드 종료
def play_end() :

    print("called play_end")

    # 전부 stand 처리
    dealer.play_status = "st_stand"
    for i in range(0, 3) :
        player_list[i].play_status = "st_stand"

    # 상금 받기
    getprize(winner)
    


########
# Main #
########

# init_deck()

total_chip = 0
dealer = Dealer.Dealer()
player_list = []
winner = None

make_players("Zen", "Hi-Lo")
calculate_chip()

# 게임 시작
play_deal()

play_continue()
