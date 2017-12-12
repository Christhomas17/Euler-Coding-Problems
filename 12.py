
# this works but too slow
# def get_factors(x):
# 	factors = []
# 	for i in range(1,x+1):
# 		if x % i == 0:
# 			factors.append(i)
# 	return(factors)
############


def get_factors(x):
	factors = []
	for i in range(1,x+1):
		if x % i == 0:
			factors.append(i)
	return(factors)	

# for item in [1,3,6,10,15,21,28]:
# 	print(get_factors(item), item)

# def get_factors(x):
# 	factors = [1]

# 	if x % 2 == 0:
# 		evenFacs = [i for i in range(2,x,2)]
# 		factors.extend(evenFacs)
# 	for i in range(3,x+1,2):
# 		if x % i == 0:
# 			factors.append(i)
# 	return(factors)


factors = []
i = 1

# for i in range(5):
# 	number = sum([i for i in range(0,i+1)])
# 	print(number)

while len(factors) <= 500:
	number = sum([i for i in range(1,i+1)])
	factors = get_factors(number)
	if len(factors) > 100:
		print(len(factors))
	i+= 1
	# factors = get_factors(number)
	# num1 = num2
	# num2 = number
	# print(number)

print(number)