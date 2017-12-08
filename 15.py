# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:49:11 2017

@author: tsbmath
"""

import itertools as it

#combos = list(it.product(['d','r'], repeat = 40))

maxSpot = 20

def combine_lists(list1, list2):
    return([sum(x) for x in zip(list1,list2)])


def check(index):
    x,y = index
    if x > maxSpot or y > maxSpot:
        return(False)
    else:
        return(True)

def try_path(x):
    index = [0,0]
    last = [maxSpot,maxSpot]
    for item in x:
        if item == 'd':
            index = combine_lists(index,[0,1])
        else:
            index = combine_lists(index,[1,0])
#        print(index)
        if check(index):
            if index == last:
                return(True)
            
        else:
            break
    return(False)



count = 0
for item in it.product(['d','r'], repeat = 40):
    if try_path(item):
        count += 1
        print(item)
#x = combos[3]
#try_path(x)
