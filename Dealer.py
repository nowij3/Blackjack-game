from Gamer import Gamer
import Deck as deck


class Dealer(Gamer):
    
    def __init__(self):
        self._hand = []  # 가지고 있는 카드
        self._hand_num = 0  # 가지고 있는 카드 개수
        self._hand_sum = 0  # 가지고 있는 카드의 숫자 합
        self._play_status = 'st_hit'  # 현재 게임 상태 [st_hit, st_stand, st_bust]
        self._blackjack = False
    
    def open_deal_card(self):
        # 카드 합 계산
        for i in range(2):
            self.hand_sum += deck[i][2]

        # Ace가 두 장일 경우 합계
        if self.hand_sum > 21:
            self.hand_sum -= 10

    # hit until sum reach 17
    def play(self):
        while self.hand_sum < 17:
            self.hit()
