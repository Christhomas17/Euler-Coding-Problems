from decimal import Decimal, getcontext
getcontext().prec = 100

# def get_repeating_cycle(x)
# x = 1/7
# print(x)
# x = Decimal(x)
# x = str(x)
# x = x.split('.')[1]
# # repeat = ''
# # print(x)





def get_repeating_pattern(x):
	x = Decimal(x)
	x = str(x)
	x = x.split('.')[1]
	length = len(x)
	# print(length)
	repeat = ''

	for index in range(length):

		repeat += x[index]

		lenPattern = len(repeat)
		# print(repeat, ',,,,,',x[(index+1):(index + lenPattern+1)])
		if repeat == x[(index+1):(index + lenPattern+1)]:
			# print(repeat)
			return(repeat)


x = get_repeating_pattern(1/6)
if x is  None:
	print('bad')





# for index,item in enumerate(x[2:]):
# 	repeat += item
	
# 	if 

# length = len(x)
# for index in range(length):
# 	repeat += x[index]
# 	print(repeat)


# print(x)







# for i in range(1,1000):
# 	print(Decimal(1/i))
