from Gamer import *
import CountingList
import Deck as deck


class CountingPlayer(Gamer):
    def __init__(self, name):
        super().__init__()

        self._chip_choice = 0  # 선택한 코인
        self._balance = self.INIT_MONEY  # 가진 금액
        self._counting = 0
        self.count_list = self.select_count_list(name)
        self._money_status = True
        self._play_status = 'st_hit'

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

    # 딜에서 카드 받은 경우 - 딜러클래스 별도구현 용이하게 따로만듦 >> polymorphism.. 사실 딜러클래스에서는 그냥 반복만 안하면되는...
    def open_deal_card(self):
        for i in range(2):
            ####################
            # sum card numbers
            ####################
            for j in range(13):
                if self.hand[i][1] == Deck.deck[j][1]:  # 모양, 이름, 값, 개수
                    self.hand_sum += Deck.deck[j][2]

            #####################
            # calculate counting
            #####################
            for j in range(13):
                if self.hand[i][1] == self.count_list[j][0]:
                    self.counting += self.count_list[j][1]

        if self.hand_sum > 21:
            """ 카드가 두장일 경우 21을 넘는 경우의 수는 A가 두장으로 22일때 뿐이므로 별도로 decide_ace_point 호출하지않고
            비교후 21보다 큰 경우 10을 빼는방식 (11, 1)점으로 계산하도록 함"""
            self.hand_sum -= 10

        self.is_blackjack()

    # Hit으로 카드 공개
    def open_hit_card(self):
        num_of_A = 0

        # setImage

        # calculate counting
        for i in range(13):  # 카운팅 리스트 전체에서 반복 (어떤 카운팅 리스트이든 카드는 13장으로 고정)
            if self.count_list[i][0] == self.hand[-1][1]:  # count_list에는 숫자-점수, hand에는 모양-숫자
                self.counting += self.count_list[i][1]  # 일단 running count // true count로 바꾸기
                break

        ####################
        # sum card numbers #
        ####################
        for check in self.hand:  # 가지고있는 카드에서 A개수 확인
            if 'A' in check:
                num_of_A += 1

        for i in range(13):  # deck에서 숫자에 해당하는 값을 찾아서 더함
            if self.hand[-1][1] == Deck.deck[i][0]:  # deck에는 모양-이름-값-개수
                self.hand_sum += Deck.deck[i][2]

        if num_of_A > 0:  # A를 가지고있는 경우
            self.hand_sum = self.decide_ace_point(num_of_A)

        self.is_bust()  # bust 확인

    # 다른 플레이어가 카드를 받았을 때 나의 hit/stand 여부와 상관없이 카운팅 계산에 반영하는 함수
    def others_card(self, o_card):
        # o_card == [모양, 숫자]
        # mycountlist == (e.g.)Zen[[숫자, 값], ... ]

        for i in range(12):
            # o_card의 숫자에 해당하는 카드 카운팅 적용값 찾고, 카운팅 변수에 더하기
            if o_card[1] == self.count_list[i][0]:
                self.counting += self.count_list[i][1]

    def get_true_count(self):
        true_count = self.counting / self.handler.get_remaining_card()
        return true_count

    # 카운팅 값 기반으로 Hit/Stand 여부 결정
    def make_decision(self):

        if self.hand_sum <= 11:
            self.play_status = "st_hit"
            self.hit()
            return

        elif self.hand_sum > 21:
            self.play_status = "st_bust"
            return

        elif self.hand_num == 2 and self.hand_sum == 21:
            self.blackjack = True

        elif self.hand_sum == 21:
            print('합은21인데블랙잭이아님ㅇㅅㅇ')
            self.play_status = 'st_stand'

        else:
            #################################################################
            # 여기가 아직 수정이 안되었읍니다
            #################################################################
            if self.get_true_count() > 0:
                self.play_status = "st_hit"
                self.hit()
                return
            else:
                self.stand()
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

    @property
    def play_status(self):
        return self._play_status

    @play_status.setter
    def play_status(self, new_play_status):
        self._play_status = new_play_status


if __name__ == "__main__":
    player = CountingPlayer('Hi-Lo')
    print(player.count_list)
    player.deal()
    print('hand = ', player.hand)
    print('count = ', player.counting)
    player.hit()
    print('hand = ', player.hand)
    print('count = ', player.counting)
    print(player.hand_num)
    print(player.get_true_count())

