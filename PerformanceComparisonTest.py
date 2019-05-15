# -*- coding: utf-8 -*-
import Dealer
import CountingPlayer

# 블랙잭인 경우 베팅한 금액의 2.5배, 그 외엔 2배 반환
def prize_chip(player) :

    # 딜러와 비긴 경우
    if player.hand_sum == dealer.hand_sum :
        return 1 * player.chip_choice


    if player.blackjack :
        return int(2.5 * player.chip_choice)
    else :
        return 2 * player.chip_choice

    
# 재산에 상금 반영하기
def get_prize(winner_list) :

    for i in range(len(player_list)) :
        # 게임에 참여한 경우에만
        if player_list[i].has_money() :
            player_list[i].balance -= player_list[i].chip_choice

    for i in range(len(winner_list)) :
        if winner_list[i].name == 'Dealer' :
            continue
        else :
            winner_list[i].balance += prize_chip(winner_list[i])
            winner_list[i].num_of_winning +=1

# hit 상태인 플레이어가 남아있는지 확인
def hit_anyone() :
    
    for i in range(len(player_list)) :
        if player_list[i].is_playable() :
            return True

    # 아무도 hit하지 않으면
    return False

# 모든 플레이어가 파산 상태인지 확인
def check_all_money_status() :

    for i in range(5) :
        if player_list[i].has_money() :
            return True
    
    # 모두가 파산이면
    return False


# 게임에 참여하는 플레이어 생성
def make_players() :
    
    player_list.append(CountingPlayer.CountingPlayer("Hi-Lo"))
    player_list.append(CountingPlayer.CountingPlayer("KO"))
    player_list.append(CountingPlayer.CountingPlayer("Hi-Opt2"))
    player_list.append(CountingPlayer.CountingPlayer("Zen"))
    player_list.append(CountingPlayer.CountingPlayer("Halves"))


# 플레이어 중 블랙잭이 있는지 확인
def check_blackjack() :

    for i in range(5) :
        if player_list[i].is_blackjack() :
            winner_list.append(player_list[i])

    if dealer.is_blackjack() :
        winner_list.append(dealer)
        return True

    # 딜러 제외 플레이어 중 블랙잭이 있으면
    if winner_list :
        return True

    # 아무도 블랙잭이 아니면
    else :
        return False

# 아무도 블랙잭이 아닌 경우 21에 가장 가까운 플레이어(우승자) 찾기
def find_winner() :

    #if not check_blackjack() :
        
    # 파산 상태가 아닌 플레이어들 목록
    not_bust_list = []

    # 딜러가 파산하지 않은 상태면
    if not dealer.is_bust() : 
        not_bust_list.append(dealer)

        # 게임에 참여한 플레이어 중 하나라도 파산하지 않은 상태면
        for i in range(5) :
            if not player_list[i].is_bust() and player_list[i].has_money():
                    not_bust_list.append(player_list[i])

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

                        # 우승자가 여러명인지 확인
                        for i in range(1, len(not_bust_list)) :
                            if tmp_winner.name != not_bust_list[i].name :
                                if tmp_winner.hand_sum == not_bust_list[i].hand_sum :
                                    winner_list.append(not_bust_list[i])
                else :                   
                    winner_list.append(tmp_winner)
                    
    # 딜러가 파산하면 파산하지 않은 플레이어들 모두 우승
    else :
        for i in range(5) :
            if not player_list[i].is_bust() and player_list[i].has_money():
                winner_list.append(player_list[i])
    
# 다른 플레이어에게 내 카드 정보 주기
def give_my_card_info(num, card) :

    for i in range(5) :
        # 자기 자신은 포함하지 않기 위해 사용하는 if문
        if i != num :
            player_list[i].others_card(card)
    
# 게임 시작, 모두 초기화
def play_new_game() :

    ## print("\n***NEW GAME START***")
    
    dealer.HANDLER.reset()

    make_players()
        
    dealer.new_game()
    for i in range(5) :
        player_list[i].new_game()

    play_start()

# 게임 시작, 베팅칩만 초기화
def play_new_hand() :

    ## print("\n***NEW HAND START***")

    dealer.new_hand()
    
    for i in range(5) :
        if player_list[i].has_money :
            player_list[i].new_hand()
        
    play_start()

# 라운드 시작
def play_start() :

    del winner_list[:]

    for i in range(5) : 
        player_list[i].decide_betting()

    # 카드가 부족하면 덱을 초기화
    ##print("get_remaining_card : ", dealer.HANDLER.get_remaining_card())
    if dealer.HANDLER.get_remaining_card() <= 0.5 :
        dealer. HANDLER.reset()
        ##print("called deck_handler.reset")
        for i in range(5) :
            player_list[i].counting = 0
        
    play_deal()


# 딜
def play_deal() :
            
    # hit 가능한 상태로 초기화
    dealer.play_status = "st_hit"

    for i in range(5) :
        if player_list[i].has_money() :
            player_list[i].play_status = "st_hit"
  
    # deal
    dealer.deal()
    for i in range (5) :
        if player_list[i].is_playable() :
            player_list[i].deal()

    give_my_card_info(3, dealer.hand[0])

    for i in range (5) :
        # 카드를 받았으면 (이 부분 수정해야되나?)
        if player_list[i].hand :
            # 첫 두 장 정보 주기
            give_my_card_info(i, player_list[i].hand[0])
            give_my_card_info(i, player_list[i].hand[1])

    play_continue()

# 딜 이후 게임 진행  ***이 지점에서 문제 발생***
def play_continue() :
    
    if hit_anyone() :
        play_hit()
        
    # 모두의 hit가 끝나면
    # 딜러의 딜에서 받은 뒤집히지 않은 카드 오픈
    dealer.open_second_card()
    give_my_card_info(5, dealer.hand[1])
    
    # 딜러가 카드를 hit 할 때 마다 다른 플레이어들에게 카드 정보 주기
    while dealer.make_decision() :
        give_my_card_info(5, dealer.hand[-1])

    ##final_information()
    check_blackjack()

    play_round_end()


# 히트
def play_hit() :
  
    while hit_anyone() :
        for i in range(5) :
            if player_list[i].is_playable() :
                if player_list[i].make_decision() :
                    give_my_card_info(i, player_list[i].hand[-1])
                
# 한 라운드 종료
def play_round_end() :
          
    # winner 리스트가 비었으면
    if not winner_list :
        find_winner()

    ##print(" ")
    ##for i in range(len(winner_list)) :
        ##print("winner : ", winner_list[i].name)
    
    # 상금 받기
    get_prize(winner_list)
        

# 메인 게임 종료
def play_game_end(test_case) :

    print("\n***GAME END***")
    print("total round : ", test_case)
    print("num of winning and winning rate and balance")
    for i in range(5) :
        print(player_list[i].name,":",player_list[i].num_of_winning,",", int((player_list[i].num_of_winning/test_case) * 100), "%,",player_list[i].balance)
    print(" ")
    
# 메인 테스트 함수
def final_information() :
    
    print(dealer.name, " : ", dealer.hand ,", hand_sum : ", dealer.hand_sum, ", play_status : ", dealer.play_status)
    for i in range(5) :
        print(player_list[i].name," : ",player_list[i].hand, ", hand_sum : ", player_list[i].hand_sum, ", play_status : ", player_list[i].play_status)

def routine(test_case) :
    play_new_game()
    
    for i in range(test_case) :
        if not check_all_money_status() :
            print ("round ends at", i+1)
            play_game_end(i+1)
            return
        
        else :
            play_new_hand()


    # 실행 횟수를 채우면
    play_game_end(test_case)
    


########
# Main #
########

dealer = Dealer.Dealer()

player_list = []
winner_list = []

routine(1000)
