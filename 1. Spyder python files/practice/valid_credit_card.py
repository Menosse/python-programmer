# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:56:19 2020

@author: Fernando
"""


def create_list(list_num):
    res = [int(x) for x in str(list_num)]
    return res

def check_credit_card(number):
    valid = False
    numbers_list = create_list(number)
    other_number_list = [element * 2 for element in numbers_list[-2::-2]]
    remaining = [element for element in numbers_list[::-2]]
    sum_other_number_list = 0
    total_sum = 0
    total_modulus = 0
    for i in range(len(other_number_list)):
        aux = create_list(other_number_list[i])
        for i in range(len(aux)):
            sum_other_number_list += aux[i]    
    total_sum = sum_other_number_list + sum(remaining)    
    total_modulus = total_sum % 10
    
    if total_modulus == 0:
        valid = True
    return (valid)


# ref_num = 371449635398431

test = int(input('Enter your credit card number: '))

# test = 5502092869734615

# a = check_credit_card(ref_num)
a = check_credit_card(test)
if a == True:
    print('Este cartao eh valido')
else:
    print('Cartao invalido')