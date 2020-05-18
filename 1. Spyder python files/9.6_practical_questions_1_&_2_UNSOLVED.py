# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:17:56 2019

@author: giles
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''
# class bankAccount(object):
#     def __init__(self,balance=0.0):
#         self.balance = balance
    
#     def displayBalance(self):
#         print(f'Your account balance is {self.balance}')
    
#     def withdraw(self,amount=0.0):
#         a = str(input(f'Would you like to withdraw {amount}? Y/N: ')).lower()
#         if a == 'y':
#             if amount <= self.balance:
#                 self.balance = self.balance - amount
#                 print(f'You have withdrawn {amount}, your new balance is {self.balance}!')
#             else:
#                 print('sorry, this amount is higher than your total account balance! Your Balance is {self.balance}')
#         else:
#             print('Operation canceled')
#     def deposit(self):
#         dep = float(input(f'how much would you like to deposit? '))
#         self.balance =+ dep
#         print(f'your new balance is {self.balance}')
                
# myaccount = bankAccount()

    


'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''
import math
class circle(object):
    def __init__(self,radius=1):
        self.radius = radius
    
    def circleArea(self):
        print(f'The area is {math.pi * (self.radius**2)}')
        
my_circle = circle(3)
my_circle.circleArea()