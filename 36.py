# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:20:51 2017

@author: chris
"""
'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
from numpy import binary_repr
import numpy as np



def is_palindrome(x):
    x = str(x)
    if len(x) % 2 == 0:
        totLen = int(len(x)/2)
    else:
        totLen = int(len(x)/2)
        
    for i in range(totLen):
        
#        print(x[i],x[-(i+1)])
        if x[i] == x[-(i+1)]:
            pass
#            print(x[i],x[-(i+1)])
        else:
            return(False)
        
    return(True)
    
nums = [] 


for num in np.arange(1,1000000,1):
    if is_palindrome(num) and is_palindrome(binary_repr(num)):
        nums.append(int(num))     
        
x = sum(nums)
print(x)

