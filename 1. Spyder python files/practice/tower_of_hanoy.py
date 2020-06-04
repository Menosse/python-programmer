# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 17:48:06 2020

@author: Fernando
"""


# A = [14,13,12,11,10,9,8,7,6,5,4,3,2,1]
A = [3,2,1]
B = []
C = []

count = 0
def towers_of_hanoi(A,B,C,n):
    global count 
    
    if n == 1:
        disk = A.pop()
        C.append(disk)
        count +=1
    else:
        
        towers_of_hanoi(A,C,B,n-1)
        print(f'First call {A,B,C}')
        towers_of_hanoi(A,B,C,1)
        print(f'Second call {A,B,C}')
        towers_of_hanoi(B,A,C,n-1)
        print(f'Third call {A,B,C}')
    return count

towers_of_hanoi(A,B,C,3)