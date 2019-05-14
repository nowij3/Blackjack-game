from Deck import Deck
import random


class DeckHandler:

    def __init__(self):
        print("called handler init")
        self._n_deck=4 # deck의 수 초기값(0.5씩 차감 = 사용한 deck의 수)
        self._n_used_cards = 0 # 사용한 카드 수
        for i in range(52):
            Deck.deck[i][3]=4 # deck의 모든 카드의 개수를 4로 초기화


    def get_card(self):
        ##print("called handler get_card")

        # 0~51까지 담은 리스트를 생성한 후 랜덤하게 섞기
        self.num_list = list(range(52))
        random.shuffle(self.num_list)

        for i in range(52) :
            rand_num = self.num_list[i]
            
            if Deck.deck[rand_num][3] > 0:
                break
            
            # 리스트를 전부 돌았는데도 카드가 없다면
            if i == 51 :
                self.reset()
                
                for i in range(52) :
                    rand_num = self.num_list[i]            
                    if Deck.deck[rand_num][3] > 0:
                        break
                

        Deck.deck[rand_num][3] -= 1
        rand_card = Deck.deck[rand_num]  # 뽑은 카드 기억
        card = [rand_card[0], rand_card[1]]  # 카드의 모양과 숫자 기억
        
        self.n_used_cards += 1

        if self.n_used_cards >= 26:
            self.n_deck -= 0.5
            self.n_used_cards = 0
            
            print("self.n_deck :", self.n_deck)
            
        return card  # Suit, Denomination


    # 남은 카드 반환
    def get_remaining_card(self):
        return self.n_deck


    #초기화하는 함수
    def reset(self):
        print("called handler reset")

        self.n_deck=4 # deck의 수 초기값(0.5씩 차감 = 사용한 deck의 수)
        self.n_used_cards = 0 # 사용한 카드 수
        for i in range(52):
            Deck.deck[i][3]=4 # deck의 모든 카드의 개수를 4로 초기화


# properties

    @property
    def n_deck(self):
        return self._n_deck

    @n_deck.setter
    def n_deck(self, new_n_deck):
        self._n_deck = new_n_deck

    @property
    def n_used_cards(self):
        return self._n_used_cards

    @n_deck.setter
    def n_used_cards(self, new_n_used_cards):
        self._n_used_cards = new_n_used_cards


