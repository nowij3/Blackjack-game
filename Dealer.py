from Gamer import Gamer
import Deck as deck


class Dealer(Gamer):
    # 수정해야댐
    ''' 
        처음 한장을 공개하고, 다른플레이어들이 결정을 모두 한 이후에 마지막으로 딜러가 카드를 공개함
        그래서 지금 당장 카드를 한장밖에 공개안한상태라 17이 될수가없음
        두장째 공개한 이후에 play를 해야되는뎀
    '''
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

