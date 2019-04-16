# -*- coding: utf-8 -*-
import Gamer
import CountingList
import Deck as deck
import Dealer
import CountingPlayer

# 유저가 베팅할 칩 선택 (GUI로 인풋받기)
def user_betting(chip) :
    player[1].chip_choice += chip
    player[1].balance -= chip_choice


# 모든 플레이어가 베팅한 칩 계산해서 반환
def calculate_chip() :
    total_chip = 0
    for i in range(1, 4) :
        total_chip += player[i].chip_choice


# 블랙잭인 경우 1.5배 반환
def prize_chip(player) :
    if player.blackjack == true :
        return 1.5 * total_chip
    else :
        return total_chip
    
# 재산에 상금 반영하기
def get_prize(player) :
    player.balance += prize_chip()

# 카드 덱 초기화
def init_deck() :
    deck.reset()
    
# 게임에 참여한 플레이어들
def make_players(name1, name2) :

    # player[1]은 항상 유저로 설정
    player[1] = Gamer()
    player[2] = CountingPlayer(name1)
    player[3] = CountingPlayer(name2)


# 메인
make_players("Zen", "Hi-Lo")


