from Gamer import Gamer
import Deck as deck


class Dealer(Gamer):
    # 수정해야댐
    def open_deal_card(self):
        # 카드 합 계산
        self.hand_sum += deck[0][2]

        # Ace가 두 장일 경우 합계
        if self.hand_sum > 21:
            self.hand_sum -= 10

    # hit until sum reach 17
    def play(self):
        while self.hand_sum < 17:
            self.hit()

    # 게임 가능 여부 확인 -
    def is_playable(self):
        if self.play_status == 'st_stand':
            return True
        return False

