'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
def is_prime(x):
	return(all(x%i != 0 for i in range(2,x,1)))

for i in range(3,10,2):
	print(is_prime(i),i)