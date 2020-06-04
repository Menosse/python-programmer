# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:44:56 2020

@author: Fernando
"""


def linear_search(item, my_list):
    i = 0
    found = False
    
    while i < len(my_list) and found == False:
        if my_list[i] == item:
            found = True
        else:
            i += 1
    return found

mylist = [1,2,3,4,5,6,7,8,9,10]
test = 10

print(linear_search(test, mylist))
