'''


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

def is_prime(x):
	for i in range(2,x-1,1):
		if x % i == 0:
			return(False)
	return(True)

def is_factor(num,divisor):
	return(num%divisor == 0)

def get_factors(x):
	factors = []
	for i in range(x-1,2,-1):

		if is_factor(x,i):
			factors.append(i)
			factors.append(x/i)
	# print(factors)		
	uniques = list(set(factors))

	uniques = [int(x) for x in uniques]
	return(uniques)

def get_prime_factors(x):
	primes = []
	for item in x:
		if is_prime(item):
			primes.append(item)
	return(primes)


# print(is_prime(12345678))
factors = get_factors(600851475143)
print(factors)
# print(get_prime_factors(factors))