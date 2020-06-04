# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:07:15 2020

@author: Fernando


True = Heads
False = Tails
"""

n = 1001
# coins = [True for x in range(n)]
coins = [0]*n
# coins = [1,2,3,4,5,6,7,8,9,10]

for i in range(1,n):
    for j in range(0,n,i):
        coins[j] = 1 - coins[j]
        
# n = 1001
# coins = [0]*n

# for i in range(1,n):
#     for j in range(0,n,i):
#         coins[j] = 1 - coins[j]