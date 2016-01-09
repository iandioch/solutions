def threes(n):
	if n == 1:
		print n
	else:
		m = n % 3
		x = 0
		if m == 1:
			x = -1
		elif m == 2:
			x = +1

		print n, x
		threes((n + x)/3)

threes(31337357)