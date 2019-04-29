from Gamer import *
import CountingList
import Deck as deck


class CountingPlayer(Gamer):
    def __init__(self, name):
        super().__init__()

        self._chip_choice = 0  # 선택한 코인
        self._balance = self.INIT_MONEY  # 가진 금액
        self._money_status = True

        # GUI를 위해 알고리즘 플레이어 이름 부여
        self.name = name

        self.count_list = self.select_count_list(self.name)

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

        self.is_blackjack()

    # Hit으로 카드 공개
    def open_hit_card(self):
        num_of_A = 0

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

        ########################################################################################################
        ############# 여기 len(Deck) 수정 #######################################################################
        ########################################################################################################
        for i in range(len(deck)):  # deck에서 숫자에 해당하는 값을 찾아서 더함
            if str(self.hand[-1][1]) == deck[i][0]:  # deck에는 숫자-개수-값-모양
                self.hand_sum += deck[i][2]

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
