# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:25:58 2020

@author: Fernando

Create triagles inside triagles by transforming it:
    transformation 1:
        xn+1 = 0.5xn
        yn+1 = 0.5yn
    transformation 2:
        xn+1 = 0.5xn + 0.5
        yn+1 = 0.5yn + 0.5
    transformation 3:
        xn+1 = 0.5xn + 1
        yn+1 = 0.5yn
"""
from random import choice
from matplotlib import pyplot as plt
def trans_1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x
    y1 = 0.5 * y
    
    return x1, y1

def trans_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5
    
    return x1, y1

def trans_3(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 1
    y1 = 0.5 * y
    
    return x1, y1

transform = [trans_1,trans_2,trans_3]
a1 = [0]
b1 = [0]
a,b = 0,0

for i in range(1000000):
    trans = choice(transform)
    a,b = trans((a,b))
    a1.append(a)
    b1.append(b)
    
plt.rc('figure', figsize=(16,16))
plt.plot(a1,b1,'o')
plt.savefig('my_triagle')