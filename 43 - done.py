# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:08:54 2017

@author: chris
"""


import numpy as np
from itertools import product, permutations, chain

numbers = np.arange(0,10,1)
def is_pandigital(x):
    
    x = [i for i in x]    
    
    lenX = len(set(x))
    return(lenX == 10 )

def props(x):
#    x = str(x)
    
    if int(x[1:4]) % 2 == 0 and int(x[2:5]) % 3 == 0 and int(x[3:6]) % 5 == 0 and \
          int(x[4:7]) % 7 == 0 and int(x[5:8]) % 11 == 0 and int(x[6:9]) % 13 == 0 and \
             int(x[7:10]) % 17 == 0 :
        return(True)
    
    else:
        return(False)


good = []
for numInt in permutations(numbers, 10):
    
    num = ''.join(str(item) for item in numInt)    

    if is_pandigital(num) and props(num):
        print(num)
        good.append(int(num))
        
print(good, sum(good))