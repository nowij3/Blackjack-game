from Deck import Deck
import random


class DeckHandler:

    def __init__(self):
        self.reset()

    def get_card(self):

        while True:
            rand_num=random.randint(0,51)
            if Deck.deck[rand_num][3] > 0:
                break
        Deck.deck[rand_num][3] -= 1
        rand_card = Deck.deck[rand_num]  # 뽑은 카드 기억
        card = [rand_card[0], rand_card[1]]  # 카드의 모양과 숫자 기억
        
        self._sum+=1
        self._n_cards-=1

        if self._sum>=26:
            self._n_deck-=0.5
            self._sum=0
        
        return card  # Suit, Denomination



    def get_remaining_card(self):
          
        n_deck=self._n_deck

        return n_deck
            

              
    def reset(self):
         #초기화하는 함수
        self._n_deck=4 #deck의 수 초기값(0.5씩 차감=사용한 deck의 수)
        self._sum=0
        self._n_cards=208 #deck의 카드 수
        for i in range(52):
            Deck.deck[i][3]=4 #deck의 모든 카드의 개수를 4로 초기화
