from math import sqrt


x = '197'



def is_prime(x):
	if x == 2:
		return(True)
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
	for i in range(3,x,2):
		if is_prime(i):
			primes.append(i)

	return(primes)

primes_list = create_primes_list(1000000)
# print(primes_list)
# print('got primes')

x = 197


def rotate(x):
	x = str(x)
	length = len(x)
	indices = [i for i in range(length)]
	nums = []
	for step in range(length):
		indices = [index - 1  if index  >0 else length - 1 for index in indices]
		number = ''.join([x[index] for index in indices])
		# print(number)
		nums.append(int(number))
	return(nums)

		

# print(rotate(123))



def rotate2(x):
	x = str(x)

	if len(x) == 1:
		# print(int(x))
		return([int(x)])
	if len(x) == 2:
		first = x[0]
		second = x[1]
		num1 = int(x)
		num2 = int(second + first)
		# print(num1,num2)
		return(num1,num2)
	else:

		first = x[0]
		second = x[1]
		third = x[2]

		num1 = int(x)
		num2 = int(second + third + first)
		num3 = int(third + first + second)

		# print(num1,num2,num3)
		return(num1,num2,num3)

rotate(x)
# print(primes_list)
count = 0 
circles = []
for num in primes_list:
	# print(num)
	# print([is_prime(x) for x in rotate(num)])
	if all([is_prime(x) for x in rotate(num)]):
		# print(num)
		count += 1
		circles.append(num)
print(count)
# print(circles)
# print(count / 3)

