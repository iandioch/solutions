def get_digits(n):
	return sorted(str(n))
	
n = int(input())
digs = get_digits(n)
dig_n = len(digs)
i = n + 1
while True:
	new_digs = get_digits(i)
	if new_digs == digs:
		print (i)
		break
	elif len(new_digs) > dig_n:
		print (0)
		break
	i += 1
