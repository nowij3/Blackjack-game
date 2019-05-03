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


# 블랙잭인 경우 베팅한 금액의 2.5배, 그 외엔 2배 반환
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
def set_level() :

    print("called set_level")

    my_level = input("level : ")
    
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
def find_winner(winner) :

    print("called find_winner")
    
    if winner == None :
        if check_blackjack() == False :
            if dealer.hand_sum < 21 :
                tmp = dealer
            else :
                tmp = None
            
            for i in range(0, 3) :
                if player_list[i].hand_sum < 21 :
                    if tmp == None :
                        tmp = player_list[i]
                    elif tmp.hand_sum < player_list[i].hand_sum :
                        tmp = player_list[i]
            if tmp != None :
                winner = tmp
                return
            
        # 모두가 파산인 경우
        else :
            winner_list.append(dealer)
            return

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
    set_level()
    calculate_chip()
    play_deal()
    play_continue()

# 라운드 시작 (딜) ***딜 할 때 give_my_card_info 안되어있음
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

    dealer.open_deal_card()
    give_my_card_info(3, dealer.hand[-1])
    
    for i in range (0, 3) :
        player_list[i].open_deal_card()
        give_my_card_info(i, player_list[i].hand[-2])
        give_my_card_info(i, player_list[i].hand[-1])


# 딜 이후 게임 진행 
def play_continue() :

    print("called play_continue")

    # 딜 카드에서 블랙잭이 있는 경우
    if check_blackjack() :
        play_end()
        
    else :
        for i in range (0, 3) :
            if player_list[i].is_playable :
                player_list[i].hit()
                give_my_card_info(i, player_list[i].hand[-1])
            else :
                # hit한 플레이어가 아무도 없다면
                play_end()
                return
                
        # 딜러의 딜에서 받은 뒤집히지 않은 카드 오픈
        dealer.open_second_card()
        give_my_card_info(3, dealer.hand[-1])
        
        if check_blackjack() :
            play_end()
            return
                        
    while hit_anyone() :
        
        dealer.play()
        
        for i in range (0, 3) :
            if player_list[i].is_playable :
                player_list[i].hit()
                give_my_card_info(i, player_list[i].hand[-1])
                
        if check_blackjack() :
            break
        
            
    play_end()

# 한 라운드 종료
def play_end() :

    print("called play_end")

    # 테스트
    show_your_hand()

    # 전부 stand 처리
    dealer.play_status = "st_stand"
    for i in range(0, 3) :
        player_list[i].play_status = "st_stand"
        
    # if check_blackjack == False :
    find_winner(winner_list)

    print("winner : ", winner_list)
    
    # 상금 받기
    if not winner_list :
        get_prize(winner_list)
    
# 메인 테스트 함수
def show_your_hand() :
    
    print("called show_your_hand")
    
    print("dealer : ", dealer.hand)
    print(player_list[0].name," : ",player_list[0].hand)
    print("user : ",player_list[1].hand)
    print(player_list[2].name," : ",player_list[2].hand)
    

########
# Main #
########

deck_handler = DeckHandler.DeckHandler()
total_chip = 0
dealer = Dealer.Dealer()
player_list = []
winner_list = []

play_start()
