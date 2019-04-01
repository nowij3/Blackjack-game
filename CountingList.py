# -*- coding: utf-8 -*-

"""
카드 카운팅 알고리즘 클래스
"""

class CountingList:
    
    def __init__(self) :
    # [숫자, 카운팅적용값]
    self.Hi_Lo = [['2', 1],['3', 1],['4', 1],['5', 1], ['6', 1], ['7', 0],['8', 0],['9', 0],['10', -1],  ['J', -1],['Q', -1],['K', -1],['A', -1]]
    self.KO = [['2', 1],['3', 1],['4', 1],['5', 1], ['6', 1], ['7', 1],['8', 0],['9', 0],['10', -1],  ['J', -1],['Q', -1],['K', -1],['A', -1]]
    self.Hi_Opt2 = [['2', 1],['3', 1],['4', 2],['5', 2], ['6', 1], ['7', 1],['8', 0],['9', 0],['10', -2],  ['J', -2],['Q', -2],['K', -2],['A', 0]]
    self.Zen = [['2', 1],['3', 1],['4', 2],['5', 2], ['6', 2], ['7', 1],['8', 0],['9', 0],['10', -2],  ['J', -2],['Q', -2],['K', -2],['A', -1]]
    self.Halves = [['2', 0.5],['3', 1.0],['4', 1.0],['5', 1.5], ['6', 1.0], ['7', 0.5],['8', 0],['9', -0.5],['10', -1],  ['J', -1],['Q', -1],['K', -1],['A', -1]]


    def get_Hi_Lo(self) :
        return self.Hi_Lo
    
    def get_KO(self) :
        return self.KO
    
    def get_Hi_Opt2(self) :
        return self.Hi_Opt2
    
    def get_Zen(self) :
        return self.Zen
    
    def get_Halves(self) :
        return self.Halves
