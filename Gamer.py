# -*- coding: utf-8 -*-

""""
게이머클래스
"""

import Deck as deck
import random

##############################################################################################
# chip_choice가 현재 balance보다 많은경우 제재 필요
# 헬퍼기능 넣을때 유저는 어떤 카운팅 사용하는지
# name은 ( 'Hi-Lo', 'KO', 'Hi-Opt2', 'Zen', 'Halves' ) 대소문자, 하이픈주의
# 카드에서 문제생기면 리스트 시작을 2가아니라 'A'로 잡아서일 가능성... 원소비교(?)로 한것같긴한데 혹시모르니 메모
##############################################################################################

#############################################################
# deck, playing_deck 구별
#############################################################


class Gamer:
    INIT_MONEY = 10000  # 시작금

    def __init__(self):
        self._hand = []  # 가지고 있는 카드
        self._hand_num = 0  # 가지고 있는 카드 개수
        self._hand_sum = 0  # 가지고 있는 카드의 숫자 합
        self._play_status = 'st_hit'  # 현재 게임 상태 [st_hit, st_stand, st_bust]
        self._blackjack = False

    # 게임 재시작. 게임 전체 초기화
    def new_game(self):
        # 전체변수 재설정
        self.new_hand()

    def new_hand(self):
        # self.get_chip()   # 칩 받는 부분 구현 필요
        self.hand = []
        self.hand_num = 0
        self.hand_sum = 0
        self.play_status = 'st_hit'
        self.blackjack = False

        self.deal()

    # 카드 받기
    def get_card(self, playing_deck):
        ################################
        # deck reset 적용할때 수정
        ################################
        while True:
            rand_num = random.randint(0, 13)  # 카드 랜덤 선택 (13장 카드 기준)
            if playing_deck[rand_num][1] > 0:  # deck에 해당 카드가 없으면 다시 뽑기
                break

        playing_deck[rand_num][1] -= 1  # 뽑은 카드 한장을 덱에서 제외
        rand_card = playing_deck[rand_num]  # 뽑은 카드 기억
        card = [rand_card[0], rand_card[1]]  # 카드의 모양과 숫자 기억
        return card  # Suit, Denomination

    # 딜
    def deal(self, playing_deck):
        if self.money_status:
            self.balance -= self.chip_choice

            # 카드 두 장 뒤집기
            self.hand[self.hand_num] = self.get_card(playing_deck)
            self.hand_num += 1
            self.hand[self.hand_num] = self.get_card(playing_deck)
            self.hand_num += 1

        return self.hand

    # 카드 공개
    def open_card(self):

        # Hit으로 카드 공개
        if self.hand_num > 2:
            self.open_hit_card()

        # 처음 Deal로 카드를 두장 받은상태
        elif self.hand_num == 2:
            self.open_deal_card()

        # 카드 한장이하(오류)
        else:
            print("wrong card number")

    # Hit. 카드 추가로 받기
    def hit(self):
        if self._play_status == "st_hit":
            self._hand[self._hand_num] = self.get_card()
            self._hand_num += 1
            self.open_card()

    # Stand. 카드 더이상 받지 않음
    def stand(self):
        self._play_status = "st_stand"

    # Ace 카드 점수 결정
    ''' deck에서 A값을 11로 설정하고 합이 21을 넘을경우 10을빼서 1로 만드는방법으로'''
    def decide_ace_point(self, num_of_ace):
        if self.hand_sum > 21:
            for i in range(num_of_ace):
                self.hand_sum -= 10
                if self.hand_sum <= 21:
                    break

        return self.hand_sum

    # 딜에서 카드 받은 경우
    def open_deal_card(self):
        for i in range(2):
            # setImage
            self.hand_sum += deck[i][2]

        if self.hand_sum > 21:
            """ 카드가 두장일 경우 21을 넘는 경우의 수는 A가 두장으로 22일때 뿐이므로 별도로 decide_ace_point 호출하지않고
            비교후 21보다 큰 경우 10을 빼는방식 (11, 1)점으로 계산하도록 함"""
            self.hand_sum -= 10

        self.is_blackjack()

    def open_hit_card(self):
        num_of_A = 0

        # setImage

        ####################
        # sum card numbers #
        ####################
        for check in self.hand:  # 가지고있는 카드에서 A개수 확인
            if 'A' in check:
                num_of_A += 1

        ########################################################################################################
        ############# 여기 len(Deck) 수정 #######################################################################
        ########################################################################################################
        for i in range(len(DECK)):  # deck에서 숫자에 해당하는 값을 찾아서 더함
            if str(self.hand[-1][1]) == deck[i][0]:  # deck에는 숫자-개수-값-모양
                self.hand_sum += deck[i][2]

        if num_of_A > 0:  # A를 가지고있는 경우
            self.hand_sum = self.decide_ace_point(num_of_A)

        self.is_bust()  # bust 확인

    # 합이 21을 초과하는지 검사하고 초과하면 play_status 변경
    def is_bust(self):
        if self.hand_sum > 21:
            self.play_status = 'st_bust'

    # 처음 두장의 합이 21인 경우 (BlackJack인 경우)
    def is_blackjack(self):
        if self.hand_num == 2 and self.hand_sum == 21:
            self.blackjack = True
            return True
        return False

    # 잔고 확인
    def has_money(self):
        if self.balance < 100:
            self.money_status = False
            return False
        return True

    # 게임 가능 여부 확인 -
    def is_playable(self):
        if self.has_money() and self.play_status == 'st_stand':
            return True
        return False

# properties

    @property
    def chip_choice(self):
        return self._chip_choice

    @chip_choice.setter
    def chip_choice(self, new_chip_choice):
        self._chip_choice = new_chip_choice

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, new_hand):
        self._hand = new_hand

    @property
    def hand_num(self):
        return self._hand_num

    @hand_num.setter
    def hand_num(self, new_hand_num):
        self._hand_num = new_hand_num

    @property
    def hand_sum(self):
        return self._hand_sum

    @hand_sum.setter
    def hand_sum(self, new_hand_sum):
        self._hand_sum = new_hand_sum

    @property
    def counting(self):
        return self._counting

    @counting.setter
    def counting(self, new_counting):
        self._counting = new_counting

    @property
    def play_status(self):
        return self._play_status

    @play_status.setter
    def play_status(self, new_play_status):
        self._play_status = new_play_status

    @property
    def money_status(self):
        return self._money_status

    @money_status.setter
    def money_status(self, new_money_status):
        self._money_status = new_money_status

    @property
    def blackjack(self):
        return self._blackjack

    @blackjack.setter
    def blackjack(self, new_blackjack):
        self._blackjack = new_blackjack
