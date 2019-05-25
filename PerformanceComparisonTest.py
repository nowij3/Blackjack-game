# -*- coding: utf-8 -*-
import Dealer
import CountingPlayer



# 블랙잭인 경우 베팅한 금액의 2.5배, 그 외엔 2배 반환
def prize_chip(player) :

    # 딜러와 비긴 경우
    if player.hand_sum == dealer.hand_sum :
        return player.chip_choice


    if player.is_blackjack() :
        return int(2.5 * player.chip_choice)
    else :
        return 2 * player.chip_choice

    
# 재산에 상금 반영하기
def get_prize() :

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
            blackjack_winner_list[i].num_of_winning += 1

    # 블랙잭이 아닌 우승자
    for i in range(len(winner_list)) :
        if winner_list[i].name == 'Dealer' :
            continue
        else :
            winner_list[i].balance += prize_chip(winner_list[i])
            winner_list[i].num_of_winning += 1

    # 비긴 플레이어
    for i in range(len(draw_list)) :
        draw_list[i].balance += prize_chip(draw_list[i])

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


# 게임에 참여하는 플레이어 생성
def make_players() :
    
    player_list.append(CountingPlayer.CountingPlayer("Hi-Lo"))
    player_list.append(CountingPlayer.CountingPlayer("KO"))
    player_list.append(CountingPlayer.CountingPlayer("Hi-Opt2"))
    player_list.append(CountingPlayer.CountingPlayer("Zen"))
    player_list.append(CountingPlayer.CountingPlayer("Halves"))


# 플레이어 중 블랙잭이 있는지 확인
def check_blackjack() :

    for i in range(len(player_list)) :
        if player_list[i].is_blackjack() :
            blackjack_winner_list.append(player_list[i])

    # 블랙잭인 플레이어가 없을 때 딜러가 블랙잭인지 확인
    if not blackjack_winner_list and dealer.is_blackjack() :
        blackjack_winner_list.append(dealer)

    # 딜러 제외 플레이어 중 블랙잭이 있으면
    if winner_list :
        return True

    # 아무도 블랙잭이 아니면
    else :
        return False

# 아무도 블랙잭이 아닌 경우 21에 가장 가까운 플레이어(우승자) 찾기
def find_winner() :

    # 블랙잭 우승자 찾기
    check_blackjack()

    for i in range(len(player_list)) :

        # 블랙잭이 아닌 플레이어만 확인
        if not player_list[i].is_blackjack() :

            # 플레이어가 파산이면 딜러 우승
            if player_list[i].is_bust() and not dealer.is_blackjack() :
                winner_list.append(dealer)

            # 딜러가 파산인 경우
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
    
# 다른 플레이어에게 내 카드 정보 주기
def give_my_card_info(num, card) :

    for i in range(len(player_list)) :
        # 자기 자신은 포함하지 않기 위해 사용하는 if문
        if i != num :
            player_list[i].others_card(card)
    
# 게임 시작, 모두 초기화
def play_new_game() :

    ## print("\n***NEW GAME START***")
    
    dealer.HANDLER.reset()

    make_players()
        
    dealer.new_game()
    for i in range(len(player_list)) :
        player_list[i].new_game()

    play_start()

# 게임 시작, 베팅칩만 초기화
def play_new_hand() :

    ## print("\n***NEW HAND START***")

    dealer.new_hand()
    
    for i in range(len(player_list)) :
        if player_list[i].has_money :
            player_list[i].new_hand()
        
    play_start()

# 라운드 시작
def play_start() :

    # 우승자 리스트 비우기
    del blackjack_winner_list[:]
    del winner_list[:]
    del draw_list[:]

    for i in range(len(player_list)) : 
        player_list[i].decide_betting()
        
    play_deal()


# 딜
def play_deal() :

    # deck에 8장 이하만 남으면 덱을 초기화
    # 카운팅 플레이어의 카운팅 초기화
    if dealer.HANDLER.get_remaining_card() <= 0.5 :
        dealer.HANDLER.reset()
    for i in range(len(player_list)) :
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

    give_my_card_info(len(player_list)+1, dealer.hand[0])

    for i in range (len(player_list)) :
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
    give_my_card_info(len(player_list)+1, dealer.hand[1])
    
    # 딜러가 카드를 hit 할 때 마다 다른 플레이어들에게 카드 정보 주기
    while dealer.make_decision() :
        give_my_card_info(5, dealer.hand[-1])

    ##final_information()
    play_round_end()


# 히트
def play_hit() :
  
    while hit_anyone() :
        for i in range(len(player_list)) :
            if player_list[i].is_playable() and player_list[i].make_decision(dealer.hand[0]) :
                give_my_card_info(i, player_list[i].hand[-1])
                
# 한 라운드 종료
def play_round_end() :
          
    # 우승자 찾기
    find_winner()

    # 상금 받기
    get_prize()


# 테스트 케이스 만큼 반복 실행하는 함수
def routine(test_case) :

    # *** 테스트할 때 본인 파일 경로로 바꾸세요 ***    
    f = open("C:/Users/JIWON01/Desktop/Result.txt",'a')

    play_new_game()
    
    for i in range(test_case) :
        play_new_hand()


    # 실행 횟수를 채우면
    for i in range(5) :
        result = player_list[i].name+" : "+str(player_list[i].num_of_winning)+", "+str(round((player_list[i].num_of_winning / test_case) * 100, 2)) +"%, "+str(player_list[i].balance)+"\n"
        f.write(result)
    f.write("\n\n")
    
    f.close()


########
# Main #
########

dealer = Dealer.Dealer()
player_list = []
blackjack_winner_list = []
winner_list = []
draw_list = []

routine(10000)