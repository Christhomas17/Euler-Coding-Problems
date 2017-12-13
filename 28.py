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
size = 1001

df = np.matrix(np.zeros(shape = (size,size)))
# print(df)
# x = [2,2]
# df[x] = 100
# print(df)

def find_middle(x):
	rows,cols = x.shape
	mid = [(rows-1)/2,(cols-1)/2 ]
	x,y = mid
	return(int(x),int(y))

middle = find_middle(df)


df[middle] = 1


maxDistance = int(size/2)


directions = [(0,1),(1,0),(0,-1), (-1,0), (0,1)]

def move(num1, num2):
    return(tuple((sum(x) for x in zip(num1,num2))))

def get_distance(spot):
    return(max([abs(x1 - x2) for (x1,x2) in zip(spot,middle)]))

def paint(df):
    spot = middle
    distance = 0
    index = 2
    while distance <= maxDistance:
        distance += 1
        for direction in directions:
            newSpot = move(spot,direction)
            try:
                while get_distance(newSpot) <= distance:
                    spot = newSpot
                    df[spot] = index
                    index += 1
                    newSpot = move(spot,direction)
                    # print(df)
            except:
                print('we out')
                return(df)

    print(df)

x =paint(df)
print(x)

def sum_diags(df):
    totSum = sum([int(df[i,i]) for i in range(size)])
    totSum += sum([int(df[(size-1) - i,i]) for i in range(size)])
    totSum -= int(df[middle])
    print(totSum)

sum_diags(x)

    
