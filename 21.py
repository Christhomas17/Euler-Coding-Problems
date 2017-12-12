def get_factors(x):
	factors = []
	for i in range(1,x):
		if x % i == 0:
			factors.append(i)
	return(factors)	

indices = []
totSums = []
myList = [i for i in range(1,10000)]


def is_amicable(index):
	global amicables
	global myList
	indexSum = sum(get_factors(index))

	partnerSum = sum(get_factors(indexSum))
	# print(get_factors(index),index,indexSum,partnerSum)
	if index == partnerSum :#and index != indexSum:


		amicables.append(indexSum)
		amicables.append(partnerSum)
		# print(indexSum,partnerSu)
		# print(amicables)
		# myList.pop(index)
		# myList.pop(partnerSum)
	# return(index == partnerSum)

amicables = []
for i in myList:
	is_amicable(i)

print(amicables)
print(len(amicables))
print(set(amicables))
print(sum(set(amicables)))
		
# print(sum(amicables))

# is_amicable(220)
