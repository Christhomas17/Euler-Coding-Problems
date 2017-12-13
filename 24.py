from itertools import permutations

x = ''.join([str(i) for i in range(10)])
# print(x)

index = []
for num in permutations(x):
	# print(num)
	index.append(int(''.join([item for item in num])))


x = sorted(index)
print(x[999999])
# print(index)
# print(sorted(index))