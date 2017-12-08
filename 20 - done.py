def factorial(x):
	totProd = 1
	for i in range(x,0,-1):
		totProd *= i

	return(totProd)


def sum_digits(x):
	x= str(x)
	totSum = 0

	for item in x:
		totSum += int(item)
	return(totSum)
# print(factorial(6))
print(sum_digits(factorial(100)))