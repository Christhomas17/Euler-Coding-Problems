num = 49
denom = 98

import re

def in_common(num,denom):
	num = [x for x in str(num)]
	denom = [x for x in str(denom)]

	if len(set(num)) == 1 or len(set(denom)) == 1:
		return(None)
	else:

		for item in num:
			if item in denom:
				return(item)
			
	return(None)
		


def check_new(num,denom,factor):
	old = num/denom

	num = str(num)
	denom = str(denom)

	num, denom = [int(re.sub(factor,'',item)) for item in [num,denom]]
	try:
		new = num/denom
	except:
		return(False)

	return(new == old)

def is_trivial(num,denom):
	if num % 10 == 0 and denom % 10 == 0:
		return(True)
	elif num == denom:
		return(True)


# x = '43'
# print(re.sub('4','',x))

# x= in_common(num, denom)
# print(x)
# print(type(x))
# print(check_new(num,denom,x))

from itertools import product
theGoods = []
numItems = 99
for perm in product([i for i in range(10,numItems+1)], repeat = 2):
	num, denom = perm
	if num < denom:
		# print(num,denom)

		x = in_common(num, denom)
		if x is not None:
			if check_new(num, denom, x):
				if not is_trivial(num, denom):
					theGoods.append(num/denom)

print(theGoods)

from functools import reduce
print(reduce(lambda x,y: x*y, theGoods))

#convert the decimal to a fration, i.e. 100