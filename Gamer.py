# -*- coding: utf-8 -*-
from module import *
class Gamer :
    
_chip_choice           # 코인 선택
_balance               # 가진 금액
INIT_MONEY = 10000     # 시작금

_hand                  # 손에 든 카드
_hand_num              # 가진 카드 개수
_hand_sum              # 가진 카드 합
_counting              # 카운팅 결과 합

_play_status           # 현재 게임 상태 (st_hit, st_stand, st_bust)
_money_status          # 현재 재산 상태 (True, False)

def __init__(self, deck) :
    self._balance = self.INIT_MONEY
    self._hand = []
    self._hand_num = 0
    self._hand_sum = 0
    self._counting = 0
    self._play_status = "st_hit"
    self._money_status = True

    # deck.__init__()

def new_game() :
    return
    
def new_hand(self, card) :
    self.get_chip()
    self.deal()

def get_card() :
    return

def deal(self) :
    if self._money_status == True :
        self._balance -= self._chip_choice

        # 카드 두 장 뒤집기
        self._hand[self._hand_num] = get_card()
        self._hand_num += 1
        self._hand[self._hand_num] = get_card()
        self._hand_num += 1

        return self._hand
    
def open_card() :
    return

def stand(self) :
    self._play_status == "st_stand"
    return self._play_status
   
def hit(self) :
    if self._play_status == "st_hit" :
        self._hand[self._hand_num] = get_card()
        self._hand_num += 1
        self._open_card()
        
