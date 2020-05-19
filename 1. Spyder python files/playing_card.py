# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:23:33 2020

@author: Fernando
"""

from random import randint

def cardValue():
    dic_value = {0:"A", 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:10, 10:'J', 11:'Q', 12:'K'}
    card_value = dic_value[randint(0,12)]

    return card_value
def cardSuit():
    dic_suit = {1:'Clubs',2:'Hearts',3:'Spades',4:'Diamonds'}
    card_suit = dic_suit[randint(1,4)]
    
    return card_suit

class PlayCard(object):
    def __init__(self):
        
        self.value = cardValue()
        self.suit = cardSuit()
    
    def display_card(self):
        
        print(f'{self.value} of {self.suit}')
    
    def get_suit(self):
        print(f'self.suit')
        
    def get_value(self):
        print(f'self.suit')
        
    # def __str__(self):
    #     my_card = str(self.value) + ' of ' + str(self.suit)
    #     return my_card

for i in range(10):
    a = PlayCard()
    a.display_card()