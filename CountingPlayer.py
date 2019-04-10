# -*- coding: utf-8 -*-
import random
import Gamer
import CountingList

class CountingPlayer(Gamer):
    def __init__(self, name):
        super.__init__(self)

        # GUI를 위해 알고리즘 플레이어 이름 부여
        self.name = name
        
        self.count_list = super.select_count_list(self.name)
        
    # 카운팅 알고리즘 적용
    def card_count(self):
        for i in range(self.hand_num) :
            
            # count_list == [숫자, 카운팅적용값]
            # hand == [숫자, 갯수, 값, 모양]
            
            if self.count_list[i][0] == self.hand[self.hand_num-1][0]:
                self.hand_count += self.count_list[i][1]
                break
            i += 1

    # 카운팅 알고리즘을 적용한 값 반환
    def get_hand_count(self) :
        return self.hand_count
