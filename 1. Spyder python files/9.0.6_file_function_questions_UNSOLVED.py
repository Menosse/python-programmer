# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:15:24 2019

@author: giles
"""

# Exercises

'''
Question 1
Create a function that will calculate the sum of two numbers. Call it sum_two.
'''
# def sum_two(a,b):
#     return a + b
# a, b = 10, 11
# print(sum_two(a,b))

'''
Question 2
Write a function that performs multiplication of two arguments. By default the
function should multiply the first argument by 2. Call it multiply.
'''
# def multiply(a,b=2):
#     return a * b
# a = 10
# print(multiply(a))
# a, b = 10, 11
# print(multiply(a,b))

'''
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.
'''
# def power(a,b=2):
#     return a ** b
# a = 6
# print(power(a))
# a, b = 6, 11
# print(power(a,b))

'''
Question 4
Create a new file called capitals.txt , store the names of five capital cities
in the file on the same line.
'''

# file = open('capitals.txt', 'w')
# file.write('London, ')
# file.write('Paris, ')
# file.write('Madrid, ')
# file.write('Lisbon, ')
# file.write('Rome, ')
# file.close()


'''
Question 5
Write some code that requests the user to input another capital city.
Add that city to the list of cities in capitals. Then print the file to
the screen.
'''
# c = str(input('please type a capital: '))
# file = open('capitals.txt', 'a')
# file.write(f'{c}, ')
# file.close()

'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''
def copy_file(file1,file2):
    original = open(file1,'r')
    copy = open(file2,'w')
    
    copy.write(original.read())
    
    original.close()
    copy.close()

copy_file('capitals.txt', 'copycapitals.txt')

