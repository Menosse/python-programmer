# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:47:21 2020

@author: Fernando
"""

import pdb

def add_num(L):
    i = 0
    size = len(L)
    total = 0
    pdb.set_trace()
    while i < size:
        total += L[i]
        i += 1
    return total

test = [1,2,3,4,5]
print(add_num(test))