def fib():
	
	a = 0
	b = 1

	i = 2
	cont = True
	value = 0 
	while cont:
		value = a + b
		a = b
		b = value

		i+= 1
		if len(str(value)) >= 1000:
			cont = False
	

	return(value,i-1)

print(fib())