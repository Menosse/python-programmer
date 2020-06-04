# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:55:30 2020

@author: Fernando
"""


def binary_search(item, search_list):
    found = False
    first = 0
    last = len(search_list) - 1
    
    while first <= last and found == False:
        midpoint = (first + last) // 2
        if search_list[midpoint] == item:
            found = True
        else:
            if search_list[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint + 1
    return found
        
    
test = [1,2,3,4,5,6,7,8,9,10]
item = 3
print(binary_search(item, test))
print(binary_search(88, test))