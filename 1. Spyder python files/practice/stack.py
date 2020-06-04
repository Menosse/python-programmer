# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:34:24 2020

@author: Fernando



def check_key(self, item):
        if item in self.dict_check:
            return True
        else:
            return False
        
    def key_by_value(self, item):
        key = ''
        for k, v in self.dict_check.items():
            if v == item:
                key = k
        return key
    
    def check_value(self, item):
        if item in self.dict_check.values():
            return True
        else:
            return False
        

Solution Control

# dict_check = {"[":"]","{":"}","(":")"}
# my_stack = []

# def check(s):
#     for i in s:
#         if i in dict_check.keys():
#             my_stack.append(i)
#         else:
#             if len(my_stack) == 0 or dict_check[my_stack.pop()] != i:
#                 return False
#     return len(my_stack) == 0

# print(check(test_string))
"""


# stack = []

# stack.append(4)
# stack
# print(stack)

# stack.append(7)
# stack
# print(stack)

# stack.pop()
# stack
# print(stack)

# class Stack():
#     def __init__(self):
#         self.list_stack = []
    
#     def is_empty(self):
#         if not self.list_stack:
#             return True
#         else:
#             return False
        
#     def push(self, item):
#         self.list_stack.append(item)
        
#     def pop(self):
#         return self.list_stack.pop()
    
#     def peek(self):
#         if self.list_stack == []:
#             return None
#         else:
#             return self.list_stack[-1]
#     def __repr__(self):
#         return repr(self.list_stack)
    
    
# new_stack = Stack()

# new_stack.is_empty()

# new_stack.push(4)
# new_stack.peek()

# new_stack.push(7)
# print(new_stack)
# new_stack.peek()


# # new_stack.is_empty()

# # new_stack.pop()



# '''


# Practice


# '''

class Stack():
    
    def __init__(self, input_string):
        self.dict_check = {"[":"]","{":"}","(":")"}
        self.my_stack = []
        self.input_string = input_string

    def __repr__(self):
        return repr(self.my_stack)
    
    def check(self):
        for i in self.input_string:
            if i in self.dict_check.keys():
                self.my_stack.append(i)
            else:
                if len(self.my_stack) == 0 or self.dict_check[self.my_stack.pop()] != i:
                    return False
        return len(self.my_stack) == 0
    
# 
test_string = "{([])}"
# test_string = "}{([])}"
# test_string = "([])}"
# test_string = "{(][)}"
# test_string = "{(["

a = Stack(test_string)
print(a.check())
    
