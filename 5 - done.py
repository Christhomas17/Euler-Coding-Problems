'''


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''



### this is a solution for a smaller number but it takes too long for a larger so we need to optimize
# import numpy as np

# maxNum = 10
# nums = np.arange(2,maxNum+ 1,1)

# number = 2520
# print(all([number % num == 0 for num in nums]) == True)

# number = 2
# while all([number % num == 0 for num in nums]) == False:
# 	if number % 10000 == 0:
# 		print(number)
# 	number += 1

# print(number)

#############################

from math import sqrt

def is_prime(x):
	if x % 2 == 0:
		return(False)
	else:
		i = 3
		#the biggest factor it can have is the sqrt of the number
		while i**2 <= x:
			if x % i == 0:
				return(False)
			else:
				i += 2

		return(True)


def create_primes_list(x):	
	primes = [2]	
	for i in range(3,int(sqrt(x)),2):
		if is_prime(i):
			primes.append(i)

	return(primes)



def get_prime_factors(numbers):
	goodDividers = []
	old = numbers
	for divisor in primes_list:
		
		new = [int(num / divisor)  if num % divisor == 0 else num for num in old]
		while new != old:
			old = new
			goodDividers.append(divisor)
			new = [int(num / divisor)  if num % divisor == 0 else num for num in old]

		if new == [1]*len(new):
			# print('hi')
			return(goodDividers)

x = 20
digits = [i for i in range(1,x+1,1)]
primes_list = create_primes_list(10000000000)
print(digits, primes_list)
primeFactors = get_prime_factors(digits)
print(primeFactors)
from functools import reduce
totProd = reduce(lambda x,y : x*y, primeFactors)
print(totProd)
# 



































# from functools import reduce
# maxNum = 4
# print(reduce(lambda x,y: x*y, [i for i in range(maxNum+1)]))




# from operator import mul
# from functools import reduce	

# # print(reduce(lambda x,y : x*y,nums))

# # z = [2,3,4]
# # print(list(lambda x,y: x*y for x,y in z))

# # h = reduce(lambda x,y : x*y, [i for i in range(1,maxNum + 1,1)])
# # print(h)
# # print(type(h))


# reducers = [19,18,17,16,15,14,13,12,11]

# # from itertools import permutations

# # for item in permutations(np.arange(1,21,1), 19):
# # 	print(item)


# number = 20
# while all([number % num == 0 for num in reducers]) == False:
# 	if number % 10000 == 0:
# 		print(number)
# 	number += 2

