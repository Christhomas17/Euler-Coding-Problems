# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:28:18 2017

@author: tsbmath
"""

import numpy as np

numbers = np.arange(1,1000000,1)

def do(x):
    count = 1
    while x != 1:
        if x % 2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        count += 1
#        print(count,x)
    return(count)

maxCount = 1
maxNumber = 1

for number in numbers:
    numCount = do(number)
    if numCount > maxCount:
        maxCount = numCount
        maxNumber = number
        print(number,maxCount,maxNumber)
        
print(maxCount)
