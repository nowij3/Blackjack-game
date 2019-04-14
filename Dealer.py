import Gamer
import Deck as deck


class Dealer(Gamer):

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
