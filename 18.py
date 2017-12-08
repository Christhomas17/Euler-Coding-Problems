# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:41:35 2017

@author: tsbmath
"""

import pandas as pd
import numpy as np
data = pd.read_table('18 - sample.txt', header = None)


def get_number_from_string(x):
    digit = ''
    numbers = []
    for index,symbol in enumerate(x):
#        print(symbol)
        if symbol != ' ':
            digit = digit + symbol
        else:
            numbers.append(int(digit))
            digit = ''
    numbers.append(int(digit))
            
#    print(numbers)
    return(numbers)
    
h = get_number_from_string(x)    

def convert_to_matrix(x):   
    numCols = len(x)
    
    df = pd.DataFrame()
#    df = np.matrix(np.zeros(shape = (numCols,numCols)))
    
    for i in range(numCols):
        
#        print(x[0][i])
        line = x[0][i]
        line = get_number_from_string(line)
        print(line)
#        df.append(line)
j = convert_to_matrix(data)
        
#convert_to_matrix(x)

#with open('18 - sample.txt', 'r') as file:
#    for item in file:
#        print(item)