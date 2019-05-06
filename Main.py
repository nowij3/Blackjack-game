# -*- coding: utf-8 -*-
import Deck as deck
import DeckHandler
import Gamer
import Dealer
import User
import CountingPlayer


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


# 블랙잭인 경우 베팅한 금액의 2.5배, 그 외엔 2배 반환 *** 카드2장 블랙잭에 대한 구별 필요
def prize_chip(player) :

    print("called prize_chip")
    
    if player.blackjack == true :
        return 2.5 * player.chip_choice
    else :
        return 2 * player.chip_choice

    
# 재산에 상금 반영하기
def get_prize(winner_list) :

    print("called get_prize")
    
    for i in range(len(winner_list)) :
        if winner_list[i].name == 'dealer' :
            continue
        else :
            winner_list[i].balance += prize_chip(winner_list[i])

# hit 상태인 플레이어가 남아있는지 확인
def hit_anyone() :
    
    print ("called hit_anyone")

    if not dealer.is_playable and not player_list[0].is_playable and not player_list[1].is_playable and not player_list[2].is_playable :
        return False
    else :
        return True
    

# 난이도 설정
def set_level(my_level) :

    print("called set_level")
    
    if my_level == "easy" :
        make_players("Hi-Lo", "KO")
    elif my_level == "normal" :
        make_players("Hi-Opt2", "Zen")
    elif my_level == "hard" :
        make_players("Halves", "Halves")
    else :
        print("잘못된 난이도 선택입니다.")


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
        if player_list[i].is_blackjack() :
            winner_list.append(player_list[i])
            return True

    if dealer.is_blackjack() :
        winner_list.append(dealer)
        return True

    # 아무도 블랙잭이 아니면
    return False

# 아무도 블랙잭이 아닌 경우 21에 가장 가까운 플레이어(우승자) 찾기
def find_winner() :

    print("called find_winner")

    # 파산 상태가 아닌 플레이어들 목록
    not_bust_list = []

    # 딜러가 파산하지 않은 상태면
    if not dealer.is_bust : 
            not_bust_list.append(dealer)

    # 플레이어 중 하나라도 파산하지 않은 상태면 
    for i in range(3) :
        if not player_list[i].is_bust :
                not_bust_list.append(dealer)

    # not_bust_list 가 비어있다면
    if not not_bust_list :
            # 모두 파산인 경우 딜러가 우승자
            winner_list.append(dealer)
    else :
            # 임시 우승자
            tmp_winner = not_bust_list[0]

            # 파산하지 않은 플레이어가 여러 명이면
            if len(not_bust_list) > 1 :
                    for i in range(1, len(not_bust_list)) :
                            # 가장 hand_sum이 큰 플레이어가 우승
                            if tmp_winner.hand_sum < not_bust_list[i].hand_sum :
                                    tmp_winner = not_bust_list[i]
            winner_list.append(tmp_winner)	
    

# 다른 플레이어에게 내 카드 정보 주기, CountingPlayer들만 적용됨
def give_my_card_info(i, card) :

    print("called give_my_card_info")

    # 자기 자신은 포함하지 않기 위해 사용하는 if문
    if i != 0 :
        player_list[0].others_card(card)
    if i != 2 :
        player_list[2].others_card(card)
    
# 게임 시작
def play_start() :

    print("called play_start")
    
    deck_handler.reset()
    set_level("easy")
    calculate_chip()
    play_deal()
    play_continue()

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

    # dealer.open_deal_card()
    give_my_card_info(3, dealer.hand[-1])
    
    for i in range (0, 3) :
        # player_list[i].open_deal_card()
        give_my_card_info(i, player_list[i].hand[-2])
        give_my_card_info(i, player_list[i].hand[-1])

    print("*play_deal*")
    show_your_hand()

# 딜 이후 게임 진행 
def play_continue() :

    print("called play_continue")

    # 딜 카드에서 플레이어에게 블랙잭이 있는 경우
    if check_blackjack() :

        # 딜러의 딜에서 받은 뒤집히지 않은 카드 오픈
        dealer.open_second_card()
        give_my_card_info(3, dealer.hand[-1])
        play_round_end()
        return


    # 플레이어가 hit한 경우에만 카드 정보 주기
    if player_list[0].make_decision() :
        give_my_card_info(0, player_list[0].hand[-1])

    # 유저 선택
    if input("hit/stand 여부 : ") == "hit" :
        player_list[1].hit()
        give_my_card_info(1, player_list[1].hand[-1])
    else :
        player_list[1].play_status = "st_stand"


    if player_list[2].make_decision() :
        give_my_card_info(2, player_list[2].hand[-1])


    # hit한 플레이어가 아무도 없다면 (딜러 제외)
    if not player_list[0].is_playable and not player_list[1].is_playable and not player_list[2].is_playable :

        # 딜러의 딜에서 받은 뒤집히지 않은 카드 오픈
        dealer.open_second_card()
        give_my_card_info(3, dealer.hand[-1])
        play_round_end()
        return

    # hit한 플레이어가 있는 경우
    # 딜러의 딜에서 받은 뒤집히지 않은 카드 오픈
    dealer.open_second_card()
    give_my_card_info(3, dealer.hand[-1])

    play_hit()

# 히트 **여기 수정!
def play_hit() :
    print("play_hit")
    show_your_hand()
        
    if check_blackjack() :
        play_round_end()
        return

    # while hit_anyone() :
        
    for i in range (0, 3) :
        if player_list[i].is_playable :
            player_list[i].hit()
            give_my_card_info(i, player_list[i].hand[-1])

    while dealer.make_decision() :
        give_my_card_info(3, dealer.hand[-1])
                
    # if check_blackjack() : break
        
            
    play_round_end()

# 한 라운드 종료
def play_round_end() :

    print("called play_round_end")

    # 테스트
    show_your_hand()

    # 전부 stand 처리
    dealer.play_status = "st_stand"
    for i in range(0, 3) :
        player_list[i].play_status = "st_stand"
        
    #if not check_blackjack :
    find_winner()

    print("winner : ", winner_list[0].name)
    
    # 상금 받기
    if not winner_list :
        get_prize(winner_list)

# 메인 게임 종료
def play_game_end() :

    print("called play_game_end")
    
    # 모든 플레이어의 재산이 파산 상태일 때
    if not player_list[0].hasmoney and not player_list[1].hasmoney and not player_list[2].hasmoney :
        
        # GUI에서 new game 제외한 모든 버튼 선택 못 하게 구현 필요
        print("press new game")
    
# 메인 테스트 함수
def show_your_hand() :
    
    print("called show_your_hand")
    
    print("dealer : ", dealer.hand , ", hand_num : ", dealer.hand_num, ", hand_sum : ", dealer.hand_sum)
    print(player_list[0].name," : ",player_list[0].hand, ", hand_num : ", player_list[0].hand_num, ", hand_sum : ", player_list[0].hand_sum)
    print("user : ",player_list[1].hand, ", hand_num : ", player_list[1].hand_num, "hand_sum : ", player_list[1].hand_sum)
    print(player_list[2].name," : ",player_list[2].hand, ", hand_num : ", player_list[2].hand_num, ", hand_sum : ", player_list[2].hand_sum)
    

########
# Main #
########

deck_handler = DeckHandler.DeckHandler()
total_chip = 0
dealer = Dealer.Dealer()
player_list = []
winner_list = []

# play_start()
set_level("easy")
'''
# dealer.deal()
# 
# for i in range (0, 3) :
#     player_list[i].deal()
#     print("player[", i, "] hand = ", player_list[i].hand)
#     print("player[", i, "] hand sum = ", player_list[i].hand_sum, '\n\n')
# 
# dealer.open_second_card()
# print("dealer hand = ", dealer.hand)
# print("dealer hand sum = ", dealer.hand_sum)
# 
# give_my_card_info(3, dealer.hand[-1])
'''

# for i in range(0, 3):
#     player_list[i].hit()
#     give_my_card_info(i, player_list[i].hand[-2])
#     give_my_card_info(i, player_list[i].hand[-1])

print("*******************play_deal****************************")
play_deal()
dealer.open_second_card()
print("*****************showing hand****************************")
show_your_hand()
