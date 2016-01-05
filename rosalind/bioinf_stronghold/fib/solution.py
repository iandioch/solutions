def getNumRabbits(desMonth, mult):
	a = 1
	b = 1
	c = 4
	for x in range(3, desMonth):
		a, b = b, c
		c = a*mult+b
	return c


print getNumRabbits(35, 3)