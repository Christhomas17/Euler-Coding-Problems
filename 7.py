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



primes = [2]
i = 2
while len(primes) < 10001:
	if is_prime(i):
		primes.append(i)

	i += 1

print(len(primes), primes[-1])
# print(primes)