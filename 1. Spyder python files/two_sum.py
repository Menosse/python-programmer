# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:24:51 2020

@author: Fernando
"""


a_list = [2,5,3,7,4]

target = 10

def two_numbers(a_list, target=10):
    d = {}
    
    for i in range(len(a_list)):
        if target - a_list[i] in d:
            print(d)
            return [d[target-a_list[i]],i]
        d[a_list[i]] = i
    return(-1)

print(two_numbers(a_list, target))
