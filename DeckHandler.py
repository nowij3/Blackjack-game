import Deck as deck
import random

class DeckHandler:

    def __init__(self):
        self._deck=4 #deck의 개수
        self._n_deck=4 #사용한 deck 수
        self._sum=0
        self._n_cards=208 #deck의 카드 수

        while True:
            rand_num=random.randint(0,13)
            if deck[rand_num][1]>0:
                break
        deck[rand_num][1]-=1
        rand_card = deck[rand_num]  # 뽑은 카드 기억
        card = [rand_card[0], rand_card[1]]  # 카드의 모양과 숫자 기억
        
        self._sum+=1
        self._n_cards-=1

        if self._sum>=26:
            self._n_deck-=0.5
            self._sum=0
        
        return card  # Suit, Denomination


###########################
# remaining card
###########################
            n_deck=self._n_deck

        return n_deck
            

              
     def reset(self):
         #초기화하는 함수
         self._deck=4
         self._n_deck=0
         self._sum=0
         self._n_cards=208
