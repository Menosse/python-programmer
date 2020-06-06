# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:09:54 2020

@author: Fernando
"""
from time import process_time
from random import randint


def insertion_sort(my_list):
    n = len(my_list)
    for i in range(1,n):
        value = my_list[i]
        j = i
        while j > 0 and my_list[j - 1] > value:
            my_list[j] = my_list[j-1]
            j = j - 1
        my_list[j] = value
    return my_list
    
def bubble_sort(my_list):
    swap_again = True
    n = len(my_list)
    while n > 0 and swap_again == True:
        n = n - 1
        swap_again == False
        
        for i in range(n):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                swap_again = True
    return my_list  

# Create a list of 50000 integers
test_list = [randint(0,50000) for integer in range(50000)]


# Interstion sort
start = process_time()
insertion_sort(test_list)
end = process_time()
total = end - start


# Bubble sort
start1 = process_time()
bubble_sort(test_list)
end1 = process_time()
total1 = end1 - start1

# Print the results
print(f'Insertion Sort time: /n start: {start} /n end: {end} /n total: {total}')
print(f'Bubble Sort time: /n start: {start1} /n end: {end1} /n total: {total1}')