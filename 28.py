'''


Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

'''

import numpy as np
its = 1000

df = np.matrix(np.zeros(shape = (its+1,its+1)))

def find_middle(x):
	rows,cols = x.shape
	mid = [(rows-1)/2,(cols-1)/2 ]
	x,y = mid
	return(int(x),int(y))

middle = find_middle(df)

x,y = middle
start = middle
df[x,y] = 1

directions = [[0,1],[1,0],[0,-1],[-1,0]]

def get_distance(list1,list2):
	return(max([abs(x1 -x2) for (x1,x2) in zip(list1,list2)]))

def sumLists(list1, list2):
    return([sum(x) for x in zip(list1,list2)])
    
#distance = 2


def move(index,distance,df,count): 
    maxRow,maxCol = df.shape
    maxRow -= 1
    maxCol -=1
    for direction in directions:
        while True:
            tempIndex = sumLists(direction,index)
#            print('temp',tempIndex,get_distance(tempIndex,start),distance)
            
            if get_distance(tempIndex,start) <= distance:
                
                x,y = tempIndex
                count += 1
                if df[x,y] == 0:
                    df[x,y] = count
                index = tempIndex
                
#                print(index)
            else:                
                break
                
#    print(df)
    return(df, index,count)

#create the matrix        
index = start
count = 1
for it in range(1,900,1):
#    print(it)
#    it = 4
    df,index,count = move(index,it,df,count)
#    print(df)

#def sum_diag(df):
#    totSum = 0
#    for i in range(its):
#        print(i)
#        totSum += df[i,i]
#        totSum += df[its-i- 1,i]
#    x,y = middle    
#    totSum = totSum - df[x,y]
#    return(totSum)
#    
#x = sum_diag(df)
