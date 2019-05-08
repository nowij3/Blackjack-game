<<<<<<< HEAD
# -*- coding: utf-8 -*-
import DeckHandler
import Dealer
import CountingPlayer

# 모든 플레이어가 베팅한 칩 계산해서 반환
def calculate_chip() :

    for i in range(5) :
        player_list[i].balance -= player_list[i].chip_choice
    
    total_chip = 0
    for i in range(5) :
        total_chip += player_list[i].chip_choice
    return total_chip


# 블랙잭인 경우 베팅한 금액의 2.5배, 그 외엔 2배 반환
def prize_chip(player) :

    # 딜러와 비긴 경우
    if player.hand_sum == dealer.hand_sum :
        return 1 * player.chip_choice


    if player.blackjack :
        return 2.5 * player.chip_choice
    else :
        return 2 * player.chip_choice

    
# 재산에 상금 반영하기
def get_prize(winner_list) :
    
    for i in range(len(winner_list)) :
        if winner_list[i].name == 'Dealer' :
            continue
        else :
            winner_list[i].balance += prize_chip(winner_list[i])
            winner_list[i].num_of_winning += 1

# hit 상태인 플레이어가 남아있는지 확인
def hit_anyone() :
    hit_flag = False

    for i in range(5) :
        if player_list[i].is_playable() :
            hit_flag = True
        
    if hit_flag :
        return True
    else :
        # 아무도 hit하지 않으면
        return False

# 모든 플레이어가 파산 상태인지 확인
def check_all_money_status() :
    money_flag = False

    for i in range(5) :
        if player_list[i].has_money() :
            money_flag = True
            
    if money_flag :
        return True
    else :
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

        # 플레이어 중 하나라도 파산하지 않은 상태면 
        for i in range(5) :
            if not player_list[i].is_bust() :
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
            if not player_list[i].is_bust() :
                winner_list.append(player_list[i])
    
# 다른 플레이어에게 내 카드 정보 주기
def give_my_card_info(num, card) :

    for i in range(5) :
        # 자기 자신은 포함하지 않기 위해 사용하는 if문
        if i != num :
            player_list[i].others_card(card)
    
# 게임 시작, 모두 초기화
def play_new_game() :

    print("***new game start***\n")
    
    deck_handler.reset()

    make_players()
        
    dealer.new_game()
    for i in range(5) :
        player_list[i].new_game()

    play_start()

# 게임 시작, 베팅칩만 초기화
def play_new_hand() :

    print("\n***new hand start***\n")

    dealer.new_hand()
    
    for i in range(5) :
        player_list[i].new_hand()
        
    play_start()

# 라운드 시작
def play_start() :

    del winner_list[:]

    for i in range(5) :        
        #유저 제외한 플레이어들에게 베팅칩 입력받기
        for i in range(5) :
            player_list[i].decide_betting()
        
    play_deal()


# 딜
def play_deal() :  
    
    # deck에 8장 이하만 남으면 덱을 초기화
    if deck_handler.get_remaining_card() <= 0.5 :
        deck_handler.reset()

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
        
        # 카드를 받았으면
        if player_list[i].hand :
            # 첫 두 장 정보 주기
            give_my_card_info(i, player_list[i].hand[0])
            give_my_card_info(i, player_list[i].hand[1])
            
    play_continue()

# 딜 이후 게임 진행 
def play_continue() :

    if hit_anyone() :
        play_hit()

    # 모두의 hit가 끝나면
    # 딜러의 딜에서 받은 뒤집히지 않은 카드 오픈
    dealer.open_second_card()
    give_my_card_info(3, dealer.hand[1])

    # 딜러가 카드를 hit 할 때 마다 다른 플레이어들에게 카드 정보 주기
    while dealer.make_decision() :
        give_my_card_info(3, dealer.hand[-1])

    final_information()    
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

    for i in range(len(winner_list)) :
        print("winner : ", winner_list[i].name)
    
    # 상금 받기
    get_prize(winner_list)
        

# 메인 게임 종료
def play_game_end(num_of_round) :

    print("***game end***")
    print("num of winning and winning rate")
    for i in range(5) :
        print(player_list[i].name," : ",player_list[i].num_of_winning," ", player_list[i].num_of_winning/num_of_round, "\n")
    
    
# 메인 테스트 함수, 딜러가 카드 두 장 이상 오픈했을 때
def final_information() :
    
    print("final information")
    
    print(dealer.name, " : ", dealer.hand ,", hand_sum : ", dealer.hand_sum)
    for i in range(5) :
        print(player_list[i].name," : ",player_list[i].hand, ", hand_sum : ", player_list[0].hand_sum, ", play_status : ", player_list[0].play_status, "\n")

def routine(test_case) :
    play_new_game()
    num_of_round = 1
    
    while num_of_round < test_case :
        play_new_hand()
        num_of_round+=1

    # 실행 횟수를 채우면
    play_game_end(num_of_round)
    


########
# Main #
########

deck_handler = DeckHandler.DeckHandler()
dealer = Dealer.Dealer()
player_list = []
winner_list = []

routine(5)
=======
# -*- coding: utf-8 -*-
import DeckHandler
import Dealer
import CountingPlayer

# 모든 플레이어가 베팅한 칩 계산해서 반환
def calculate_chip() :

    for i in range(5) :
        player_list[i].balance -= player_list[i].chip_choice
    
    total_chip = 0
    for i in range(5) :
        total_chip += player_list[i].chip_choice
    return total_chip


# 블랙잭인 경우 베팅한 금액의 2.5배, 그 외엔 2배 반환
def prize_chip(player) :

    # 딜러와 비긴 경우
    if player.hand_sum == dealer.hand_sum :
        return 1 * player.chip_choice


    if player.blackjack :
        return 2.5 * player.chip_choice
    else :
        return 2 * player.chip_choice

    
# 재산에 상금 반영하기
def get_prize(winner_list) :
    
    for i in range(len(winner_list)) :
        if winner_list[i].name == 'Dealer' :
            continue
        else :
            winner_list[i].balance += prize_chip(winner_list[i])
            winner_list[i].num_of_winning += 1

# hit 상태인 플레이어가 남아있는지 확인
def hit_anyone() :
    hit_flag = False

    for i in range(5) :
        if player_list[i].is_playable() :
            hit_flag = True
        
    if hit_flag :
        return True
    else :
        # 아무도 hit하지 않으면
        return False

# 모든 플레이어가 파산 상태인지 확인
def check_all_money_status() :
    money_flag = False

    for i in range(5) :
        if player_list[i].has_money() :
            money_flag = True
            
    if money_flag :
        return True
    else :
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

        # 플레이어 중 하나라도 파산하지 않은 상태면 
        for i in range(5) :
            if not player_list[i].is_bust() :
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
            if not player_list[i].is_bust() :
                winner_list.append(player_list[i])
    
# 다른 플레이어에게 내 카드 정보 주기
def give_my_card_info(num, card) :

    for i in range(5) :
        # 자기 자신은 포함하지 않기 위해 사용하는 if문
        if i != num :
            player_list[i].others_card(card)
    
# 게임 시작, 모두 초기화
def play_new_game() :

    print("***new game start***\n")
    
    deck_handler.reset()

    make_players()
        
    dealer.new_game()
    for i in range(5) :
        player_list[i].new_game()

    play_start()

# 게임 시작, 베팅칩만 초기화
def play_new_hand() :

    print("\n***new hand start***\n")

    dealer.new_hand()
    
    for i in range(5) :
        player_list[i].new_hand()
        
    play_start()

# 라운드 시작
def play_start() :

    del winner_list[:]

    for i in range(5) :        
        #유저 제외한 플레이어들에게 베팅칩 입력받기
        for i in range(5) :
            player_list[i].decide_betting()
        
    play_deal()


# 딜
def play_deal() :  
    
    # deck에 8장 이하만 남으면 덱을 초기화
    if deck_handler.get_remaining_card() <= 0.5 :
        deck_handler.reset()

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
        
        # 카드를 받았으면
        if player_list[i].hand :
            # 첫 두 장 정보 주기
            give_my_card_info(i, player_list[i].hand[0])
            give_my_card_info(i, player_list[i].hand[1])
            
    play_continue()

# 딜 이후 게임 진행 
def play_continue() :

    if hit_anyone() :
        play_hit()

    # 모두의 hit가 끝나면
    # 딜러의 딜에서 받은 뒤집히지 않은 카드 오픈
    dealer.open_second_card()
    give_my_card_info(3, dealer.hand[1])

    # 딜러가 카드를 hit 할 때 마다 다른 플레이어들에게 카드 정보 주기
    while dealer.make_decision() :
        give_my_card_info(3, dealer.hand[-1])

    final_information()    
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

    for i in range(len(winner_list)) :
        print("winner : ", winner_list[i].name)
    
    # 상금 받기
    get_prize(winner_list)
        

# 메인 게임 종료
def play_game_end(num_of_round) :

    print("***game end***")
    print("num of winning and winning rate")
    for i in range(5) :
        print(player_list[i].name," : ",player_list[i].num_of_winning," ", player_list[i].num_of_winning/num_of_round, "\n")
    
    
# 메인 테스트 함수, 딜러가 카드 두 장 이상 오픈했을 때
def final_information() :
    
    print("final information")
    
    print(dealer.name, " : ", dealer.hand ,", hand_sum : ", dealer.hand_sum)
    for i in range(5) :
        print(player_list[i].name," : ",player_list[i].hand, ", hand_sum : ", player_list[0].hand_sum, ", play_status : ", player_list[0].play_status, "\n")

def routine(test_case) :
    play_new_game()
    num_of_round = 1
    
    while num_of_round < test_case :
        play_new_hand()
        num_of_round+=1

    # 실행 횟수를 채우면
    play_game_end(num_of_round)
    


########
# Main #
########

deck_handler = DeckHandler.DeckHandler()
dealer = Dealer.Dealer()
player_list = []
winner_list = []

routine(5)
>>>>>>> 2ec0404a1acc27a5dbd116b0d61ffc55b58dbf34
