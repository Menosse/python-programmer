# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:51:29 2020

@author: Fernando
"""


# import string
# print(string.ascii_lowercase[:])
# print(string.ascii_lowercase[15])
# print(string.ascii_lowercase[20])


def media(x,y):
    return (x+y)/2

a, b = media(1,5), media(5,9)
c, d = media(1,9), media(3,7)
e, f = media(a,b), media(c,d)
g = media(e,f)
# a = media(media(media(1,5),media(5,9)),media(media(1,9),media(3,7)))
print(a, b, c, d)
print(e,f)
print(g)
