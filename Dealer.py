from Gamer import Gamer
from Deck import Deck


class Dealer(Gamer):

    def __init__(self):
        super().__init__()
        self.name = 'Dealer'

    # 처음 카드 한 장 공개
    def open_deal_card(self):
        # 카드 합 계산
        for i in range(13):
            if self.hand[0][1] == Deck.deck[i][1]:
                self.hand_sum += Deck.deck[i][2]
                break
        if __name__ == "__main__":
            print(self.hand[0][1])

    # 다른 플레이어들의 카드 결정이 모두 끝난 후 딜러의 두번째 카드 공개
    def open_second_card(self):
        for i in range(13):
            if self.hand[1][1] == Deck.deck[i][1]:
                self.hand_sum += Deck.deck[i][2]
                break

        if __name__ == "__main__":
            print(self.hand[1][1])

        # Ace가 두 장일 경우 합계
        if self.hand_sum > 21:
            self.hand_sum -= 10

    # hit until sum reach 17
    def make_decision(self):
        if self.hand_sum < 17:
            self.hit()
            if self.hand_sum > 21:
                self.play_status = 'st_bust'
            return True
        else:
            if not self.is_bust():
                self.stand()
            return False



    # 게임 가능 여부 확인 -
    def is_playable(self):
        if self.play_status == 'st_hit':
            return True
        return False


if __name__ == '__main__':
    dealer = Dealer()

    for i in range(10):
        dealer.new_hand()
        dealer.deal()
        dealer.open_second_card()
        print(dealer.hand)
        print(dealer.hand_sum)
        while dealer.make_decision():
            print("loop: ", dealer.hand)
            print(dealer.hand_sum)
        print(dealer.hand)
        print('sum:', dealer.hand_sum)
        print(dealer.play_status)
        print("-------------------------------------------------------------------------------")
