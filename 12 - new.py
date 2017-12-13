# def triangle_numbers(index):
# 	return(sum([i for i in range(1,index+1,1)]))

# def get_factors(x):
# 	factors = []
# 	for i in range(1,int((x+1)/2)):
# 		if x % i == 0:
# 			factors.append(i)
# 	return(factors)	


# i = 1000000

# numDivisors = 1

# while numDivisors <=500:
# 	numbers = triangle_numbers(i)
# 	factors = get_factors(numbers)
# 	numDivisors = len(factors)*2
# 	# print(numDivisors, factors, triangle_numbers(i) )
# 	i+=1 


# 	if i % 1000 == 0:
# 		print(i,numDivisors)

# print(numbers,factors, len(factors))


# print(triangle_numbers(5))



import time
 
def num_divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors
 
def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, num_divisors(n+1)
    return n
 
start = time.time()
index = find_triangular_index(500)
triangle = (index * (index + 1)) / 2
elapsed = (time.time() - start)
 
print ("result %s returned in %s seconds." % (triangle,elapsed))