# -*- coding: utf-8 -*-
import random

class Zen :
    # 카드 덱 [이름, 개수, 값]
    deck = [['A', 4, 1], ['2', 4, 2],['3', 4, 3],['4', 4, 4],['5', 4, 5], ['6', 4, 6],
            ['7', 4, 7],['8', 4, 8],['9', 4, 9],['10', 4, 10], ['J', 4, 10],['Q', 4, 10],['K', 4, 10]]
    
    zen_count = [['A', -1], ['2', 1],['3', 1],['4', 2],['5', 2], ['6', 2],
                ['7', 1],['8', 0],['9', 0],['10', -2],  ['J', -2],['Q', -2],['K', -2]]
    
    def __init__(self):
        self.hit = True
        
        self.hand = []      # 손에 든 카드
        self.hand_num = 0   # 가진 카드 개수
        self.hand_sum = 0   # 가진 카드값의 합
        self.hand_count = 0 # 카드 카운팅 알고리즘 적용

    def open_card(self):
        while True :
            # 카드 종류
            r = random.randrange(0, 13)
            if self.deck[r][1] > 0 :
                # 카드 덱에서 해당 카드빼기
                self.deck[r][1]-= 1
                break
            
        # 뽑은 카드 손에 들기
        self.hand.append(self.deck[r])
        self.hand[self.hand_num][1] = 1
        
        self.hand_sum += self.hand[self.hand_num][2]
        self.hand_num += 1
        
    # 카운팅 알고리즘 적용    
    def card_count(self):
        for i in range(self.hand_num) :
            if self.zen_count[i][0] == self.hand[self.hand_num-1][0]:
                self.hand_count += self.zen_count[i][1]
                break
            i += 1
            
    # 카운팅 알고리즘을 적용한 값 반환
    def get_hand_count(self) :
        return self.hand_count
    
    def play(self) :
        if self.hit :
            self.open_card()
            self.card_count()
            print(self.get_hand_count())
            if self.get_hand_count()>0 :
                self.hit = True
                print("Hit!")
            else :
                self.hit = False
                print("Stand!")
    
