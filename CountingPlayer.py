# -*- coding: utf-8 -*-
import random
from Gamer import Gamer
import CountingList

class CountingPlayer(Gamer):
    def __init__(self, name):
        super().__init__()

        # GUI를 위해 알고리즘 플레이어 이름 부여
        self.name = name
        
        self.count_list = self.select_count_list(self.name)
        
         # 이름에 따른 카운팅 리스트 반환
    def select_count_list(self, name):
        c_list_instance = CountingList.CountingList()
        return {'Hi-Lo': c_list_instance.get_Hi_Lo(), 'KO': c_list_instance.get_Ko(), 'Hi-Opt2': c_list_instance.get_Hi_Opt2(),
                'Zen': c_list_instance.get_Zen(), 'Halves': c_list_instance.get_Halves()}[name]

        
    # 카운팅 알고리즘 적용
    def card_count(self):
        for i in range(self.hand_num) :
            
            # count_list == [숫자, 카운팅적용값]
            # hand == [숫자, 갯수, 값, 모양]
            
            if self.count_list[i][0] == self.hand[self.hand_num-1][0]:
                self.hand_count += self.count_list[i][1]
                break

    # 카운팅 알고리즘을 적용한 값 반환
    def get_hand_count(self) :
        return self.hand_count

