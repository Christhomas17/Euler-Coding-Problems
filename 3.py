'''


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

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





x = 13195
primes_list = create_primes_list(1000000)
# print(primes_list)


def get_factors(x, primes_list):
	for num in primes_list:
		if x % num == 0:
			return(num, int(x/num))

def get_prime_factors2(x):
	primes = []
	for num in primes_list:
		num1,num2 = get_factors(num, primes_list)
		for num in [num1,num2]:
			if is_prime(num):
				primes.append(num)		
			else:
				pass

def get_prime_factors(x):
	factors = []
	div = 2

	while div * div <= x:
		while x % div == 0:
			factors.append(div)
			x = x / div
		div += 1

	if x > 1:
		factors.append(x)
	return([int(item) for item in factors])

print(get_prime_factors(600851475143 ))
# print(get_factors(20))


# myList = [i for i in range(20)]

# for index,item in enumerate(myList):
# 	if index % 3 == 0:
# 		myList.pop(index)

# print(myList)