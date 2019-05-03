from Gamer import *
import CountingList
import Deck as deck


class CountingPlayer(Gamer):
    def __init__(self, name):
        super().__init__()

        self._chip_choice = 0  # 선택한 코인
        self._balance = self.INIT_MONEY  # 가진 금액
        self._money_status = True
        self._counting = 0
        self.count_list = self.select_count_list(name)

    # 이름에 따른 카운팅 리스트 반환
    def select_count_list(self, name):
        c_list_instance = CountingList.CountingList()

        if name == 'Hi-Lo':
            return c_list_instance.get_Hi_Lo()
        elif name == 'KO':
            return c_list_instance.get_Ko()
        elif name == 'Hi-Opt2':
            return c_list_instance.get_Hi_Opt2()
        elif name == 'Zen':
            return c_list_instance.get_Zen()
        elif name == 'Halves':
            return c_list_instance.get_Halves()

        else:
            print("wrong player name")

        return [['A', '0'], ['2', '0'], ['3', '0'], ['4', '0'], ['5', '0'], ['6', '0'], ['7', '0'], ['8', '0'],
                ['9', '0'], ['10', '0'], ['J', '0'], ['Q', '0'], ['K', '0']]

    # 다른 플레이어가 카드를 받았을 때 나의 hit/stand 여부와 상관없이 카운팅 계산에 반영하는 함수
    def others_card(self, o_card):
        # o_card == [모양, 숫자]
        # mycountlist == (e.g.)Zen[[숫자, 값], ... ]

        for i in range(12):
            # o_card의 숫자에 해당하는 카드 카운팅 적용값 찾고, 카운팅 변수에 더하기
            if o_card[1] == self.count_list[i][0]:
                self.counting += self.count_list[i][1]

    # 카운팅 알고리즘 적용
    def card_count(self):
        for i in range(self.hand_num):
            for j in range(12):

                # count_list == [숫자, 카운팅적용값]
                # hand == [숫자, 갯수, 값, 모양]

                if self.hand[i][0] == self.count_list[j][0]:
                    self.counting += self.count_list[i][1]
                    break

    # 카운팅 알고리즘을 적용한 값 반환
    def get_hand_count(self):
        return self.hand_count

    def get_true_count(self):
        true_count = self.counting() / (deck.get_original_deck() - deck.get_used_deck())
        return true_count

    # 카운팅 값 기반으로 Hit/Stand 여부 결정
    def make_decision(self):

        if self.hand_sum <= 11:
            self.play_status = "st_hit"
            super().hit()
            return

        elif self.hand_sum > 21:
            self.play_status = "st_bust"
            return

        elif self.hand_sum == 21:
            self.blackjack = True

        else:
            if self.get_true_count() > 0:
                self.play_status = "st_hit"
                super().hit()
                return
            else:
                super().stand()
                return

    # 잔고 확인
    def has_money(self):
        if self.balance < 100:
            self.money_status = False
            return False
        return True

    # 게임 가능 여부 확인
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
