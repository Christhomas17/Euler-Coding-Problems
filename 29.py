a = 100
b = a

a = [i for i in range(2,a+1)]
b = [i for i in range(2,b+1)]


from itertools import product

values = []
for perm in product(a,b):
	x,y = perm
	values.append(x**y)

values = set(values)
values = sorted(values)
print(len(values))
# print(values)