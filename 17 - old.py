# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:57:22 2017

@author: tsbmath
"""

numbers = {1:'one', 
           2: 'two',
           3: 'three',
           4:'four',
           5:'five',
           6:'six',
           7:'seven',
           8:'eight',
           9:'nine',
           10:'ten',
           11:'eleven',
           12:'twelve',
           13:'thirteen',
           14:'fourteen',
           15:'fifteen',
           16:'sixteen',
           17:'seventeen',
           18:'eighteen',
           19:'nineteen',
           20:'twenty',
           30:'thirty',
           40:'fourty',
           50:'fifty',
           60:'sixty',
           70:'seventy',
           80:'eighty',
           90:'ninety',
           100:'hundred',
           1000:'onethousand'}



import numpy as np
totalLength = 0
for number in np.arange(1,1000+1,1):
    if len(str(number)) == 3:        
        numberLength = len(numbers[int(str(number)[0])]) + len(numbers[100]) + len('and')
        print(numberLength, number)
        if number % 100 != 0:
            try:
                digits = int(str(number)[1:3])                
                numberLength += len(numbers[digits])
            except:
                first = int(str(number)[1] + '0')
                second = int(str(number)[2])
                numberLength += len(numbers[first]) + len(numbers[second])
    else:
        try:
            numberlength = len(numbers[number])
        except:
            first = int(str(number)[0] + '0')
            second = int(str(number)[1])
            numberLength = len(numbers[first]) + len(numbers[second])
            
    print(number, numberLength)
    totalLength += numberLength
    
print(totalLength)
        
    
    
# for number in np.arange(1,1000,1):
#    if len(str(number)) == 3:
#        if number % 100 == 0:
#            numberLength = len(numbers[int(str(number)[0])]) + len(numbers[100]) + len('and')
#            print(numberLength, number)   
    
    
    
    
    
#    
#    
#    try:
#        print(len(numbers[number]), number)
#    except:
#        try:
#            number = str(number)
#            firstDigit = int(str(number)[0] + '0')
#            secondDigit = int(str(number)[1])
#            print(len(numbers[firstDigit]) + len(numbers[secondDigit]), number)
#        except:
#            number = int(number)
#            if number % 100 == 0:
#                totalLength += len(str(number)[0]) + len(numbers[100])
#            else:
#                number = str(number)
#                firstDigit = int(number[0])
#                totalLength += len(numbers[firstDigit]) + len(numbers[100]) + len('and')
#                
#                try:
#                    secondDigit = int(number[1:3])
#                    totalLength += len(numbers[secondDigit])
#                except:
#                    secondDigit = number[1:2] + '0'
#                    thirdDigit = number[2:3]
#       
#                    totalLength += len(numbers[secondDigit]) + len(numbers[thirdDigit])
#
##
##        

