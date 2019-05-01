# -*- coding: utf-8 -*-

""""
게이머클래스
"""

from Deck import Deck
from DeckHandler import DeckHandler

##############################################################################################
# chip_choice가 현재 balance보다 많은경우 제재 필요
# 헬퍼기능 넣을때 유저는 어떤 카운팅 사용하는지
# name은 ( 'Hi-Lo', 'KO', 'Hi-Opt2', 'Zen', 'Halves' ) 대소문자, 하이픈주의
##############################################################################################


class Gamer:
    INIT_MONEY = 10000  # 시작금

    def __init__(self):
        self._hand = []  # 가지고 있는 카드
        self._hand_num = 0  # 가지고 있는 카드 개수
        self._hand_sum = 0  # 가지고 있는 카드의 숫자 합
        self._play_status = 'st_hit'  # 현재 게임 상태 [st_hit, st_stand, st_bust]
        self._blackjack = False
        self.handler = DeckHandler()
        if __name__ == '__main__':
            print("클래스 생성")

    # 게임 재시작. 게임 전체 초기화
    def new_game(self):
        # 전체변수 재설정
        self.new_hand()
        if __name__ == '__main__':
            print("called new game")

    def new_hand(self):
        # self.get_chip()   # 칩 받는 부분 구현 필요
        self.hand = []
        self.hand_num = 0
        self.hand_sum = 0
        self.play_status = 'st_hit'
        self.blackjack = False

        self.deal()

        if __name__ == '__main__':
            print("called new_hand")

    # 딜
    def deal(self):
        if __name__ == '__main__':
            print("called deal")

        # if self.money_status:
        #     self.balance -= self.chip_choice

        # 카드 두 장 뒤집기
        self.hand.append(self.handler.get_card())
        self.hand_num += 1
        self.hand.append(self.handler.get_card())
        self.hand_num += 1

        self.open_card()

        if __name__ == '__main__':
            print("now cards = ", self.hand, "// numbers: ", self.hand_num, "// total: ", self.hand_sum)
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
        if __name__ == '__main__':
            print("called hit")

        if self.play_status == "st_hit":
            self.hand.append(self.handler.get_card())
            self.hand_num += 1
            self.open_card()

            if __name__ == '__main__':
                print("now cards = ", self.hand, "// numbers: ", self.hand_num, "// total: ", self.hand_sum)

    # Stand. 카드 더이상 받지 않음
    def stand(self):
        self._play_status = "st_stand"
        if __name__ == '__main__':
            print("called stand")

    # Ace 카드 점수 결정
    ''' deck에서 A값을 11로 설정하고 합이 21을 넘을경우 10을빼서 1로 만드는방법으로'''
    def decide_ace_point(self, num_of_ace):
        if __name__ == '__main__':
            print('called decide_ace_point')
            print("decide before : now cards = ", self.hand, "// numbers: ", self.hand_num, "// total: ", self.hand_sum)

        if self.hand_sum > 21:
            for i in range(num_of_ace):
                self.hand_sum -= 10
                if self.hand_sum <= 21:
                    break
        if __name__ == '__main__':
            print("decide after : now cards = ", self.hand, "// numbers: ", self.hand_num, "// total: ", self.hand_sum)

        return self.hand_sum

    # 딜에서 카드 받은 경우
    def open_deal_card(self):
        if __name__ == '__main__':
            print("called open_deal_Card")

        for i in range(2):
            # setImage
            for j in range(13):
                if self.hand[i][1] == Deck.deck[j][1]:          # 모양, 이름, 값, 개수
                    # if __name__ == '__main__':
                    #     print("self.hand[", i, "][1] = Deck.deck[", j, "][1]")
                    self.hand_sum += Deck.deck[j][2]

        if self.hand_sum > 21:
            """ 카드가 두장일 경우 21을 넘는 경우의 수는 A가 두장으로 22일때 뿐이므로 별도로 decide_ace_point 호출하지않고
            비교후 21보다 큰 경우 10을 빼는방식 (11, 1)점으로 계산하도록 함"""
            self.hand_sum -= 10

        self.is_blackjack()
        if __name__ == '__main__':
            print("now cards = ", self.hand, "// numbers: ", self.hand_num, "// total: ", self.hand_sum)

    def open_hit_card(self):
        if __name__ == '__main__':
            print("called open_hit_card")
        num_of_A = 0

        # setImage

        ####################
        # sum card numbers #
        ####################
        for check in self.hand:  # 가지고있는 카드에서 A개수 확인
            if 'A' in check:
                num_of_A += 1

        print("last card: ", self.hand[-1][1])

        for i in range(13):  # deck에서 숫자에 해당하는 값을 찾아서 더함
            if str(self.hand[-1][1]) == Deck.deck[i][1]:  # deck에는 모양-이름-값-개수
                self.hand_sum += Deck.deck[i][2]

        if num_of_A > 0:  # A를 가지고있는 경우
            self.hand_sum = self.decide_ace_point(num_of_A)

        self.is_bust()  # bust 확인
        if __name__ == '__main__':
            print("now cards = ", self.hand, "// numbers: ", self.hand_num, "// total: ", self.hand_sum)

    # 합이 21을 초과하는지 검사하고 초과하면 play_status 변경
    def is_bust(self):
        if __name__ == '__main__':
            print('called is_bust')

        if self.hand_sum > 21:
            self.play_status = 'st_bust'
            print("busted")

    # 처음 두장의 합이 21인 경우 (BlackJack인 경우)
    def is_blackjack(self):
        if self.hand_num == 2 and self.hand_sum == 21:
            self.blackjack = True
            if __name__ == '__main__':
                print("BLACKJACK")
            return True
        if __name__ == '__main__':
            print("not BLACKJACK")
        return False



# properties

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
    def play_status(self):
        return self._play_status

    @play_status.setter
    def play_status(self, new_play_status):
        self._play_status = new_play_status

    @property
    def blackjack(self):
        return self._blackjack

    @blackjack.setter
    def blackjack(self, new_blackjack):
        self._blackjack = new_blackjack


if __name__ == '__main__':
    gamer = Gamer()
    gamer.deal()
    gamer.hit()
    gamer.stand()
