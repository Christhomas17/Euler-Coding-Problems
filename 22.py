'''


Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

'''


import pandas as pd
import numpy as np

df = pd.read_table('22 - names.txt', header = None, sep = ',')
df = df.transpose()
df = df.dropna()
df = df.sort_values(0)
df.index = np.arange(0,len(df),1)


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def create_indexed_dict(x):
    tempDict = {}
    for index,item in enumerate(x):
        tempDict[item.upper()] = index + 1
    return(tempDict)
    
alphabet = create_indexed_dict(alphabet)



def get_value(x):
    value = 0
    for item in x:
        value += alphabet[item]
    return(value)
    
    


df['Value'] = df[0].apply(get_value)
df['Index'] = df.index + 1
df['Total Value'] = df['Value'] * df['Index']
totValue = df['Total Value'].sum()


