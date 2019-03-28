""""
게이머클래스
"""

import Deck as deck
import Zen as zen
import random


"""
newGame, getCard, openCard, decideAcePoint
"""


class Gamer:
    def __init__(self):
        self._chip_choice = None   # 선택한 코인
        self._balance = None      # 가진 금액
        self._hand = []     # 가지고있는 카드
        self._hand_num = 0     # 가지고있는 카드 개수
        self._hand_sum = 0     # 가지고있는 카드의 숫자 합
        self._counting = 0     # 카운팅 합산
        self._play_status = 'st_hit'      # 현재 게임 상태 [st_hit, st_stand, st_bust] 아님 그냥 int로해서 1, 2, 0하는게 쉬울까
        self._money_status = True     # 현재 재산 상태 [ True, False (베팅가능, 불가능) ]


    # 게임 재시작. 게임 전체 초기화
    def new_game(self):
        # init쓰면 미친놈되는거같은디요

        # 전체변수 재설정
        self.chip_choice = None  # 선택한 코인
        self.balance = None  # 가진 금액
        self.hand = []  # 가지고있는 카드
        self.hand_num = None  # 가지고있는 카드 개수
        self.hand_sum = None  # 가지고있는 카드의 숫자 합
        self.counting = None  # 카운팅 합산
        self.play_status = None  # 현재 게임 상태 [st_hit, st_stand, st_bust]
        self.money_status = None  # 현재 재산 상태 [ True, False (베팅가능, 불가능) ]
        
        #new_hand에서 변하지 않는 부분만 추가로 변경하고 그냥 new_hand부르는게 더 깔끔할듯

    # 흠. 흠.. 흠...
    def new_hand(self):
        pass

    # 카드 받기
    def get_card(self, deck):
        while True:
            rand_num = random.randint(0, 12)        # 카드를 랜덤으로 선택하기위해.. 일단 13장 카드 기준으로했고 카드 개수에 따라 수정해야
            if deck[rand_num][1] > 0:       # deck에 해당 카드가 없으면 다시 뽑기
                break
        deck[rand_num][1] -= 1                  # 뽑은 카드 한장을 덱에서 제외
        rand_card = deck[rand_num]              # 뽑은 카드 기억
        card = [rand_card[3], rand_card[0]]     # 카드의 모양과 숫자 기억
        return card     # Suit, Denomination

    # 딜
    def deal(self):
        pass

    # 카드 공개
    def open_card(self):
        num_of_A = 0

        # Hit으로 카드 공개
        if self.hand_num > 2:

            # setImage

            # calculate counting
            for i in range(len('''여기카운팅알고리즘리스트가들어간다고치고''')):  # zen 수정해야댐
                if zen[i][0] == str(self.hand[-1][1]):  # zen은 숫자-점수, hand에는 모양-숫자가정
                    self.counting += zen[i][1]      # 일단 running count // true count로 바꾸기
                    break

            ####################
            # sum card numbers #
            ####################
            for check in self.hand:         # 가지고있는 카드에서 A개수 확인
                if 'A' in check:
                    num_of_A += 1

            for i in range(len('''deck''')):            # deck에서 숫자에 해당하는 값을 찾아서 더함
                if str(self.hand[-1][1]) == deck[i][0]:  # deck에는 숫자-개수-값-모양
                    self.hand_sum += deck[i][2]

            if num_of_A > 0:           # A를 가지고있는 경우
                self.hand_sum = self.decide_ace_point(num_of_A)

            if self.hand_sum > 21:
                self.play_status = 'st_bust'


        # 처음 Deal로 카드를 두장 받은상태
        elif self.hand_num == 2:
            self.open_deal_card()

        # 카드 한장이하(오류)
        else:
            print("wrong card number")


    # Hit. 카드 추가로 받기
    def hit(self):
        pass

    # Stand. 카드 더이상 받지 않음
    def stand(self):
        pass

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
            self.counting += zen[i][1]  # 여기도 zen 수정해야
            self.hand_sum += deck[i][2]

        if self.hand_sum > 21:
            """ 카드가 두장일 경우 21을 넘는 경우의 수는 A가 두장으로 22일때 뿐이므로 별도로 decide_ace_point 호출하지않고
            비교후 21보다 큰 경우 10을 빼는방식 (11, 1)점으로 계산하도록 함"""
            self.hand_sum -= 10


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


if __name__ == '__main__':
    print('hello?')
    gamer = Gamer()
    print(gamer.play_status)
    gamer.play_status = 'st_bust'
    print(gamer.play_status)

