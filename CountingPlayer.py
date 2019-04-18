# -*- coding: utf-8 -*-
from Gamer import *
import CountingList
import Deck as deck

class CountingPlayer(Gamer):
    def __init__(self, name):
        super().__init__()

        # GUI를 위해 알고리즘 플레이어 이름 부여
        self.name = name
        
        self.count_list = self.select_count_list(self.name)

        
    # 이름에 따른 카운팅 리스트 반환
    def select_count_list(self, name):
        c_list_instance = CountingList.CountingList()

        if name == 'Hi-Lo':
            return c_list_instance.get_Hi_Lo()
        elif name == 'KO':
            return c_list_instance.get_Ko()
        elif name == 'Hi-Opt2':
            return c_list_instance.get_Hi_Opt2()
        elif name == 'Zen':
            return c_list_instance.get_Zen()
        elif name == 'Halves':
            return c_list_instance.get_Halves()
        
        if name != 'Dealer':
            print("Not a predetermined name")
            
        return [['A', '0'], ['2', '0'], ['3', '0'], ['4', '0'], ['5', '0'], ['6', '0'], ['7', '0'], ['8', '0'], 
                ['9', '0'], ['10', '0'], ['J', '0'], ['Q', '0'], ['K', '0']]
    
        # return         {'Hi-Lo': c_list_instance.get_Hi_Lo(), 'KO': c_list_instance.get_Ko(), 'Hi-Opt2': c_list_instance.get_Hi_Opt2(),        'Zen': c_list_instance.get_Zen(), 'Halves': c_list_instance.get_Halves()}[name]

        
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

    def get_true_count(self) :
        self.true_count = deck.get_hand_count() / (deck.get_original_deck() - deck.get_used_deck())
        return true_count



    # 카운팅 값 기반으로 Hit/Stand 여부 결정
    def make_decision(self) :
        
        if self.hand_sum <= 11 :
            self.play_status = "st_hit"
            super().hit()
            return
        
        elif self.hand_sum > 21 :
            self.play_status = "st_bust"
            return
        
        elif self.hand_sum == 21 :
            self.blackjack = True
            
        else :
            if get_true_count() > 0 :
                self.play_status = "st_hit"
                super().hit()
                return
            else :
                super().stand()
                return
