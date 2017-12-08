number = []
with open('13 - Number.txt', 'r') as file:
	for line in file:
		number.append(int(line))

print(type(number[0]))
print(number[0])
print(len(str(number[1])))

totSum = 0
for num in number:
	totSum += num

print(totSum)

# sum = 0
# for num in number:
# 	sum += num
# print(str(sum), 'sum')

# x = [2,3]
# print(sum(x))

# print(len(number[2]))
# print(number[0])
