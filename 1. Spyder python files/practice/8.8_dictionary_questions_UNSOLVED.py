# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: giles
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

# capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
#             'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
#             'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
#             'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
#             }
# x = input("Please input a country: ")
# if x in capitals:
#     print(f"This country {x} capital is {capitals[x]}")
# else: print("This country is not in the list!")

'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
# fib = {}
# a = 0
# b = 1

# for i in range(13):
#     fib[i] = a
#     a, b = b, a + b

'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''
# # Professor
# ap = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
# kp = ['Open','High','Low','Close']
# bp = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
# [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
# dp = {}
# for i in range(len(kp)):
#     dp[ap[i]] = dict(zip(kp,bp[i]))

# print(dp)

'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''


'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
# from random import randint
# from matplotlib import pyplot as plt
# import string
# a, b = [], string.ascii_lowercase

# for i in range(len(b)):
#     a.append(b[i])

# dic = {}
# for i in range(len(a)):
#     dic[a[i]] = randint(1,100)
    
# x,y = list(zip(*dic.items()))
    
# plt.bar(x,y)

'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''
cards = {}
a = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
b = ['Dimonds', 'Clubs', 'Hearts', 'Spades']
b = sorted(b)

for suit in b:
    # print(i)
    cards[suit] = a

print(cards)