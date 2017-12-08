# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:46:43 2017

@author: tsbmath
"""

x = 2**1000
totSum = 0
for item in str(x):
#    print(type(item))
#    print(type(int(item)))
    totSum +=   int(item)
    
print(totSum)
