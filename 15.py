
''' Let's use combinatorics here'''
For the example, we have a total of 4 steps to take

# import numpy as np

# size = 2
# end = [size, size]

# mat = np.matrix(np.zeros(shape = (size+1,size+1)))
# # print(mat)

# spot = [1,0]

# def down(spot):
# 	x,y = spot
# 	x += 1
# 	spot = [x,y]
# 	return(spot)

# def right(spot):
# 	x,y = spot
# 	y += 1
# 	spot = [x,y]
# 	return(spot)

# def move(direction,mat,end):
# 	spot = [0,0]
# 	goodSpot = [100,100]
# 	# print(direction)
# 	for dir in direction:

# 		if dir == 'd':
# 			spot = down(spot)
# 			x,y = spot
# 			try:
# 				mat[x,y] = 1
# 			except:
# 				return(False)
# 		else:
# 			spot = right(spot)
# 			x,y = spot
# 			try:
# 				mat[x,y] = 1
# 			except:
# 				return(False)
# 		goodSpot = spot

	
# 	if goodSpot == end:		
# 		return(True)

# 	else:
# 		return(False)


# from itertools import product, permutations,combinations

# # directions = list(product('dr', repeat = size*2))

# # rights = ['r','d'] * size	
# # downs = ['d'] * size

# # print(rights, downs)

# # dirs = rights.append(downs)
# # print(dirs)
# # count = 0
# # for i in combinations(['r','d']*size,4):
# # 	print(i)
# # 	count += 1

# # print(count)
# # print(directions)
# # print(len(set(directions)))
# # print(directions[0])


# # count = 0
# # for direction in product('dr', repeat = size*2):
# # 	if move(direction,mat,end):
# # 		count += 1

# # print(count)


# # print(directions)

# # print(spot)
# # print(down(spot))

# # x,y = spot
# # mat[x,y] = 10
# # print(mat)

# # x,y = down(spot)
# # print(x,y)
# # mat[x,y]

