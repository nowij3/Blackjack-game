# -*- coding: utf-8 -*-
import Dealer
import User
import CountingPlayer


# 유저가 베팅할 칩 선택 (GUI로 인풋받기)
def user_betting(chip) :

    player_list[1].chip_choice = chip


# 모든 플레이어가 베팅한 칩 계산해서 반환
def calculate_chip() :

    while player_list[1].is_playable() :
        user_chip = int(input("betting chip of User : "))
        if user_chip <= player_list[1].balance :
            user_betting(user_chip)
            break

        # 유저의 자산보다 더 큰 금액을 입력한 경우
        else :
            print("select again")

# 블랙잭인 경우 베팅한 금액의 2.5배, 그 외엔 2배 반환
def prize_chip(player) :

    # 딜러와 비긴 경우
    if player.hand_sum == dealer.hand_sum :
        print(player.name, "recieves ", player.chip_choice)
        return player.chip_choice

    if player.is_blackjack() :
        print(player.name, "recieves ", int(2.5 * player.chip_choice))
        return int(2.5 * player.chip_choice)
    else :
        print(player.name, "recieves ", 2 * player.chip_choice)
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

    # 블랙잭이 아닌 우승자
    for i in range(len(winner_list)) :
        if winner_list[i].name == 'Dealer' :
            continue
        else :
            winner_list[i].balance += prize_chip(winner_list[i])

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

# 난이도 설정
def set_level(my_level) :


    if my_level == "easy" :
        make_players("Hi-Lo", "KO")
    elif my_level == "normal" :
        make_players("Hi-Opt2", "Zen")
    elif my_level == "hard" :
        make_players("Halves", "Hi-Opt2")
    else :
        print("잘못된 난이도 선택입니다.")


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
                
# 다른 플레이어에게 내 카드 정보 주기, CountingPlayer들만 적용됨
def give_my_card_info(num, card) :

    # 유저와 자기 자신은 포함하지 않기 위해 사용하는 if문
    # 유저는 player_list[1]
    for i in range(len(player_list)) :
        if i != 1 and i!= num:
            player_list[i].others_card(card)

# 게임 시작, 모두 초기화
def play_new_game() :

    print("\n***NEW GAME START***")

    dealer.HANDLER.reset()

    while True :
        choice = input("select level (easy, normal, hard) : ")
        if choice != "easy" and choice != "normal" and choice != "hard" :
            print("select again")
        else :
            set_level(choice)
            break


    dealer.new_game()
    for i in range(len(player_list)) :
        player_list[i].new_game()

    play_start()

# 게임 시작, 베팅칩만 초기화
def play_new_hand() :

    print("\n***NEW HAND START***")

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

    print(" ")
    # 각자의 재산 출력
    for i in range(len(player_list)) :
        print("current balance of ",player_list[i].name, ": ", player_list[i].balance)

    print(" ")
    for i in range(len(player_list)) :
        #유저 제외한 플레이어들에게 베팅칩 입력받기
        if i != 1 :
            player_list[i].decide_betting()
            print("betting chip of ",player_list[i].name," : ", player_list[i].chip_choice)

    # 유저에게 베팅칩 입력받기
    calculate_chip()

    play_deal()


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
        give_my_card_info(len(player_list)+1, dealer.hand[-1])

    final_information()
    play_round_end()


# 히트
def play_hit() :

    while hit_anyone() :

        if player_list[1].hand_sum == 21 :
            player_list[1].play_status = "st_stand"
            
        # 유저 선택 받기
        if player_list[1].is_playable() :
            while True :
                choice = input("hit/stand : ")
                if  choice == "hit" :
                    player_list[1].play_status = "st_hit"
                    break

                elif choice == "stand" :
                    player_list[1].play_status = "st_stand"
                    break
                
                else :
                    print("select again")

        if player_list[0].is_playable() :
            # hit 한 경우에만 카드 정보 나눠주기
            if player_list[0].make_decision(dealer.hand[0]) :
                give_my_card_info(0, player_list[0].hand[-1])

        if player_list[1].is_playable() :
            player_list[1].hit()
            give_my_card_info(1, player_list[1].hand[-1])

        if player_list[2].is_playable() :
            if player_list[2].make_decision(dealer.hand[0]) :
                give_my_card_info(2, player_list[2].hand[-1])

        current_information()


# 한 라운드 종료
def play_round_end() :

    print("\n***ROUND END***\n")

    # 우승자 찾기
    find_winner()

    # 상금 받기
    get_prize()

    # 모두가 파산이면
    if not check_all_money_status() :
        play_game_end()
    else :
        play_new_hand()


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


########
# Main #
########

dealer = Dealer.Dealer()
player_list = []
blackjack_winner_list = []
winner_list = []
draw_list = []

play_new_game()


