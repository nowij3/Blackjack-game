from Gamer import Gamer
import Deck as deck


class Dealer(Gamer):
    # 처음 카드 한 장 공개
    def open_deal_card(self):
        # 카드 합 계산
        for i in range(12):
            if self.hand[0][1] == deck[i][2]:
                self.hand_sum += deck[i][2]
                break

    # 다른 플레이어들의 카드 결정이 모두 끝난 후 딜러의 두번째 카드 공개
    def open_second_card(self):
        for i in range(12):
            if self.hand[1][1] == deck[i][2]:
                self.hand_sum += deck[i][2]
                break

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

