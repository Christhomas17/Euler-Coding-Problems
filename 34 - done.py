from math import factorial

# x= 145

# y = sum([factorial(int(digit)) for digit in str(x)])


numbers = []
for num in range(3,10000000):
	if sum([factorial(int(digit)) for digit in str(num)]) == num:
		numbers.append(num)
		print(numbers)
print(sum(numbers))



