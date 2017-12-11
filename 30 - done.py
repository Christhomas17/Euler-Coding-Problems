def find_sum(x,power):
	x = str(x)

	totSum = 0

	for digit in x:
		totSum += int(digit)**power

	return(totSum == int(x))

# print(find_sum(1634,4))

values = []

for num in range(2,9999999,1):
	if find_sum(num,5):
		values.append(num)
		print(values)

print(sum(values))