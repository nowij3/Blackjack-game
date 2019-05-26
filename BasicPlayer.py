from Gamer import Gamer
from Deck import Deck

from Dealer import Dealer

"""
기본 전략을 사용하는 플레이어
"""

class BasicPlayer(Gamer):

    INIT_MONEY = 10000000

    def __init__(self):
        super().__init__()

        self._chip_choice = 0  # 선택한 코인
        self._balance = self.INIT_MONEY  # 가진 금액
        self._money_status = True
        self.name = 'Basic'
        self.num_of_winning = 0  # 성능 비교를 위한 변수

    def new_game(self):
        self.chip_choice = 0
        self.balance = self.INIT_MONEY
        self.money_status = True
        self.new_hand()
        self.num_of_winning = 0

    # 베팅금액 설정
    def decide_betting(self):
        self.chip_choice = 200

        # chip_choice가 balance보다 큰 경우
        if self.chip_choice > self.balance:
            self.chip_choice = self.balance

    def make_decision(self, dealer_card):
        dealer_hand = -1

        # 딜러 카드에 해당하는 점수 찾기
        for i in range(13):
            if dealer_card[1] == Deck.deck[i][1]:  # dealer_card [모양, 숫자] Deck [모양, 숫자, 값, 개수]
                dealer_hand = Deck.deck[i][2]

        test_list = []

        if self.hand_num == 2:
        # 핸드의 1번째 원소를 가져와서 test_list에 append, 그리고 sort
            for i in range(2):
                test_list.append(self.hand[i][1])

            test_list.sort()
        # print("my card", self.hand_sum)
        # print("dealer card", dealer_hand)
        # print(test_list)

            if test_list[1] == 'A' and (test_list[0] == '8' or test_list[0] == '9'):
                self.stand()
                print("here?")
                if __name__ == '__main__':
                    print(1)
                return False
            elif (dealer_hand == 7 or dealer_hand == 8) and (test_list[1] == 'A' and test_list[0] == '7'):
                self.stand()
                if __name__ == '__main__':
                    print(2)
                return False

        if self.hand_sum <= 11:
            self.hit()
            if __name__ == '__main__':
                print(10)
            return True
        elif self.hand_sum >= 17:
            self.stand()
            if __name__ == '__main__':
                print(11)
            return False
        elif self.hand_sum > 21:
            self.play_status = "st_bust"
            if __name__ == '__main__':
                print(12)
            return False

        elif dealer_hand >= 7 and self.hand_sum <= 16:
            self.hit()
            if __name__ == '__main__':
                print(21)
            return True

        # 카드 합 12일때
        elif self.hand_sum == 12:
            if dealer_hand == 2 or dealer_hand == 3:
                self.hit()
                if __name__ == '__main__':
                    print(22)
                return True
            elif dealer_hand in [4, 5, 6]:
                self.stand()
                if __name__ == '__main__':
                    print(23)
                return False

            else:
                # 합이 12일때, dealer카드 2 or 3
                self.hit()
                print(999)
                if __name__ == '__main__':
                    print(999)
                return True
        elif self.hand_sum < 17 and dealer_hand < 7:
            self.stand()
            if __name__ == '__main__':
                print(24)
            return False

        else:
            self.stand()
            if __name__ == '__main__':
                print('0000')
            return False

    # 잔고 확인
    def has_money(self):
        if self.balance < 100:
            self.money_status = False
            return False
        return True

    # 게임 가능 여부 확인
    def is_playable(self):
        if self.has_money() and self.play_status == 'st_hit':
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
    def money_status(self):
        return self._money_status

    @money_status.setter
    def money_status(self, new_money_status):
        self._money_status = new_money_status

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


if __name__ == "__main__":
    p = BasicPlayer()
    d = Dealer()
    # p.deal()
    # print(p.hand)
    # print(d.deal())
    #
    # while p.make_decision(d.hand[0]):
    #     print(p.hand)
    #
    # print("p hand", p.hand)
    # d.open_second_card()
    #
    # while d.make_decision():
    #     print(d.hand)
    #
    # print("d hand", d.hand)

    p.hand.append(['CLV', '8'])
    p.hand.append(['DMD', 'A'])
    p.hand_sum = 19

    d.hand.append(['SPD', '9'])
    d.hand.append(['HRT', 'K'])
    p.hand_num = 2
    p.hand_sum = 19

    p.make_decision(d.hand[0])