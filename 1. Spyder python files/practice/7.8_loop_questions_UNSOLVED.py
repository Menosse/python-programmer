#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Giles
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
# def askNumber():
#     aux = input("Please input a number between 1 - 100: ")
#     while not aux.isdigit():
#         print("Smth wrong try again.. ")
#         aux = input("Please input a number between 1 - 100: ")
#     return(int(aux))

# a = []
# a.append(askNumber())
# a.append(askNumber())
# print(sorted(a))


'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
# a = str(input("please type smth: "))
# reverse = ''
# for char in a:
#     reverse = char + reverse
#     print(reverse)
# print(a[::-1])

'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
# aux = int((input("please type a number between 1 - 12: ")))
# while aux < 1 or aux > 12:
#     print("Smth wrong try again.. ")
#     aux = int((input("please type a number between 1 - 12: ")))
# timeTable = 12
# for i in range(timeTable):
#     print(f'{i+1} times {aux} = {(i+1)*aux}')

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
# for i in range(1,13):
#     print(f'==============TIME TABLE {i}==============')
#     for j in range(1,13):
#         print(f'{i} times {j} = {i*j}')
    

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
# def askNumber():
#     aux = (input("please type a number: "))
#     while not aux.isdigit():
#         print("Smth wrong try again.. ")
#         aux = input("Please input a number between 1 - 100: ")
#     return(int(aux))

# a = []
# for i in range(5):    
#     a.append(askNumber())
# print(sum(a)/(len(a)))

'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
# def askNumber():
#     aux = (input("please type a number: "))
#     while not aux.isdigit():
#         print("Smth wrong try again.. ")
#         aux = input("Please input a number between 1 - 100: ")
#     return(int(aux))

# a = askNumber()
# for i in range(a-1,0,-1):
#     a = a*i
#     print(f'{a}*{i}={a*i}')
    

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
# fib = []
# a = 0
# fib.append(a)
# b = 1
# fib.append(b)
# for i in range(19):
#     a, b = b, a + b
#     fib.append(b)
# print(fib)



'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''



'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''
# star = '*'

# for i in range(1,7):
#     for j in range(1,6):
#         if i == 1 and j < 6:
#             print(star,end='')
#         elif i == 2 and j == 1:
#             print()
#             print(star)
#         elif i == 3 and j < 5:
#             print(star,end='')
#         elif i == 4 and j == 1:
#             print()
#             print(star)  
#         elif i == 5 and j == 1:
#             print(star)
#         elif i == 6 and j == 1:
#             print(star)   


'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
# odd = []
# even = []

# for i in range(1,101):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f'Even numbers: {even}\n\n\nOdd numbers: {odd}')