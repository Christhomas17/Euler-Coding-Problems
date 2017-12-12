

x = 20

# for i in range(2,x,1):
# 	if x % i == 0:
# 		print(i)
# 		break

def get_factors(x):
	i = 2
	factors = []

	
	print(i)
	#checks if it divides evenely
	while x % i == 0:
		#adds the factor
		factors.append(i)
		x = x/i
	# print(i)
	i += 1

	return(factors)

# print(get_factors(20))
# for i in range(16):
# 	print(i**2)

# def factors(x):
# 	i = 2
# 	factors = []

# 	while i ** 2 <= x:
# 		print(i)
# 		while x % i == 0:
# 			print('hi')
# 			factors.append(x)
# 			x = x / i

# 		i += 1

# print(factors(20))

# def prime_factors(n):
#     factors=[]
#     d=2
#     while(d*d<=n):
#         while(n>1):            
#             while n%d==0:
#                 factors.append(d)
#                 n=n/d
#             d+=1
#     return factors[-1]

# print(prime_factors(20))

# def get_factors(x):
# 	i = 2
# 	factors = []

# 	while i**2 <= x:
# 		print(i)

# 		while x % i == 0:
# 			factors.append(x)
# 			x = x / i  
# 	i += 1

# 	return(factors)

# print(get_factors(8))
# print('all done')

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


# for i in range(50):
# 	print(is_prime(i),str(i))

def create_primes_list(x):	
	primes = [2]	
	for i in range(3,int(sqrt(x)),2):
		if is_prime(i):
			primes.append(i)

	return(primes)

primes_list = create_primes_list(10000)
# print(primes_list)

# def get_prime_factors(x,primes_list):
# 	factors = []
# 	for number in primes_list:
# 		if x % number == 0:
# 			factors.append(number)
# 			factors.append(int(x/number))
# 			break
# 	primes = []
# 	for number in factors:
# 		if is_prime(number):
# 			primes.append(number)
# 		else:
# 			primes.append(get_prime_factors(number,primes_list))

# 	return(factors)

# print(get_prime_factors(20,primes_list))


# def prime_factorsa(num, factor):
# 	if num < factor:
# 		return([])
# 	if num % factor == 0:
# 		return(factor + prime_factors(num / factor,2))
# 	return(prime_factors(num, factor + 1))


# print(prime_factors(10,2))



# def prime_factors(n):
# 	factors = []
# 	div = 2
# 	while div <= n:
# 		if n % div == 0:
# 			n //= div
# 			factors.append(div)
# 		else:
# 			div += 1
# 	return(factors)

# def prime_factors(n):
# 	factors = []
# 	div = 2
	
# 	while div <= n:
# 		if n % div == 0:
# 			n //= div
# 			factors.append(div)
# 		else:
# 			div += 1
# 	return(factors)


# for i in range(2,21,1):
# 	print(prime_factors(i))


# def prime_factors_table(x)


x = [4,7,12,21,42]
goodDividers = []


# divisor = 2
# print(x)
# new = [int(num / divisor)  if num % divisor == 0 else num for num in x]
# print(new)


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
			return(goodDividers)

	
x = 10
primes_list = create_primes_list(10000000)

# print(primes_list)
# print([i for i in range(1,x+1,1)])
prime_factors = get_prime_factors([i for i in range(1,x+1,1)])
print(prime_factors)
# print('done')

# from functools import reduce

# print(reduce(lambda x,y :x*y, [i for i in range(1,x+1,1)]))


		

		




