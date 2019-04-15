# -*- coding: utf-8 -*-

""""
게이머클래스
"""

import Deck as deck
import random
from module import *        # 이건 무슨뜻이조
import CountingList


##############################################################################################
# chip_choice가 현재 balance보다 많은경우 제재 필요
# 헬퍼기능 넣을때 유저는 어떤 카운팅 사용하는지
# name은 ( 'Hi-Lo', 'KO', 'Hi-Opt2', 'Zen', 'Halves' ) 대소문자, 하이픈주의
# 카드에서 문제생기면 리스트 시작을 2가아니라 'A'로 잡아서일 가능성... 원소비교(?)로 한것같긴한데 혹시모르니 메모
##############################################################################################


class Gamer:
    INIT_MONEY = 10000  # 시작금

    def __init__(self):
        self._chip_choice = None  # 선택한 코인
        self._balance = self.INIT_MONEY  # 가진 금액
        self._hand = []  # 가지고 있는 카드
        self._hand_num = 0  # 가지고 있는 카드 개수
        self._hand_sum = 0  # 가지고 있는 카드의 숫자 합
        self._counting = 0  # 카운팅 합산
        self._play_status = 'st_hit'  # 현재 게임 상태 [st_hit, st_stand, st_bust]
        self._money_status = True  # 현재 재산 상태 [ True, False (베팅가능, 불가능) ]

#        self.count_list = self.select_count_list(name)      # 알고리즘에 따른 카운팅리스트 mycountlist얘기했는데 그냥 count_list로바꿈여

    # 게임 재시작. 게임 전체 초기화
    def new_game(self):
        # 전체변수 재설정
        self.chip_choice = None
        self.balance = self.INIT_MONEY
        self.counting = 0
        self.money_status = True

        self.new_hand()

    def new_hand(self):
        # self.get_chip()   # 칩 받는 부분 구현 필요
        self.hand = []
        self.hand_num = 0
        self.hand_sum = 0
        self.play_status = 'st_hit'

        self.deal()


    # 카드 받기
    def get_card(self, deck):
        while True:
            rand_num = random.randint(0, 13)  # 카드 랜덤 선택 (13장 카드 기준)
            if deck[rand_num][1] > 0:  # deck에 해당 카드가 없으면 다시 뽑기
                break
        deck[rand_num][1] -= 1  # 뽑은 카드 한장을 덱에서 제외
        rand_card = deck[rand_num]  # 뽑은 카드 기억
        card = [rand_card[0], rand_card[1]]  # 카드의 모양과 숫자 기억
        return card  # Suit, Denomination

    # 딜
    def deal(self):
        if self.money_status == True:
            self.balance -= self.chip_choice

            # 카드 두 장 뒤집기
            self.hand[self.hand_num] = self.get_card()
            self.hand_num += 1
            self.hand[self.hand_num] = self.get_card()
            self.hand_num += 1

        return self.hand

    # 카드 공개
    def open_card(self):
        num_of_A = 0

        # Hit으로 카드 공개
        if self.hand_num > 2:

            # setImage

            # calculate counting
            for i in range(13):  # 카운팅 리스트 전체에서 반복 (어떤 카운팅 리스트이든 카드는 13장으로 고정)
                if self.count_list[i][0] == str(self.hand[-1][1]):  # count_list에는 숫자-점수, hand에는 모양-숫자
                    self.counting += self.count_list[i][1]  # 일단 running count // true count로 바꾸기
                    break

            ####################
            # sum card numbers #
            ####################
            for check in self.hand:  # 가지고있는 카드에서 A개수 확인
                if 'A' in check:
                    num_of_A += 1

            for i in range(len('''deck''')):  # deck에서 숫자에 해당하는 값을 찾아서 더함
                if str(self.hand[-1][1]) == deck[i][0]:  # deck에는 숫자-개수-값-모양
                    self.hand_sum += deck[i][2]

            if num_of_A > 0:  # A를 가지고있는 경우
                self.hand_sum = self.decide_ace_point(num_of_A)

            self.is_bust()      # bust 확인


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
        return self._play_status

    # Ace 카드 점수 결정
    ''' deck에서 A값을 11로 설정하고 합이 21을 넘을경우 10을빼서 1로 만드는방법으로'''

    def decide_ace_point(self, num_of_ace):
        if self.hand_sum > 21:
            for i in range(num_of_ace):
                self.hand_sum -= 10
                if self.hand_sum <= 21:
                    break

        return self.hand_sum

    # 딜에서 카드 받은 경우 - 딜러클래스 별도구현 용이하게 따로만듦 >> polymorphism.. 사실 딜러클래스에서는 그냥 반복만 안하면되는...
    def open_deal_card(self):
        for i in range(2):
            # setImage
            self.counting += self.count_list[i][1]  # 카운팅 점수 계산
            self.hand_sum += deck[i][2]

        if self.hand_sum > 21:
            """ 카드가 두장일 경우 21을 넘는 경우의 수는 A가 두장으로 22일때 뿐이므로 별도로 decide_ace_point 호출하지않고
            비교후 21보다 큰 경우 10을 빼는방식 (11, 1)점으로 계산하도록 함"""
            self.hand_sum -= 10

    # 다른 플레이어가 카드를 받았을 때 나의 hit/stand 여부와 상관없이 카운팅 계산에 반영하는 함수
    def others_card(self, o_card):
        # o_card == [모양, 숫자]
        # mycountlist == (e.g.)Zen[[숫자, 값], ... ]

        for i in range(12):
            # o_card의 숫자에 해당하는 카드 카운팅 적용값 찾고, 카운팅 변수에 더하기
            if (o_card[1] == self.count_list[i][0]):
                self.counting += self.count_list[i][1]   # 여기 counting을 각각의 플레이어에게 전달해야하지않나여

    # 합이 21을 초과하는지 검사하고 초과하면 play_status 변경
    def is_bust(self):
        if self.hand_sum > 21:
            self.play_status = 'st_bust'

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
