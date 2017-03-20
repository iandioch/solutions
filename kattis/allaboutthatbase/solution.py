numtests = int(input())

bases = '123456789abcdefghijklmnopqrstuvwxyz0'
numbers = set([c for c in '123456789'])

MAXVAL = 2**32 - 1

def basetoint(v):
	if v == '0':
		return 36
	if v in numbers:
		return int(v)
	else:
		return ord(v) - ord('a') + 10


for testn in range(numtests):
	x, op, y, _, z = input().split()
	highestchar = max(x+y+z)
	poss = []
	minbase = basetoint(highestchar) + 1
	if highestchar == '1':
		minbase = 1
	for base in range(minbase, 37):
		i = len(x)
		j = len(y)
		k = len(z)
		if base > 1:
			i = int(x, base=base)
			j = int(y, base=base)
			k = int(z, base=base)
		else:
			if not len(set(x)) == len(set(y)) == len(set(z)) == 1:
				# cannot have any zeroes in base 1
				continue

		if i > MAXVAL or j > MAXVAL or k > MAXVAL:
			continue
		if i < 1 or j < 1 or k < 1:
			continue

		if op == '+' and i + j == k:
			poss.append(base)
		elif op == '-' and i - j == k:
			poss.append(base)
		elif op == '/' and i / j == k:
			poss.append(base)
		elif op == '*' and i * j == k:
			poss.append(base)
	if len(poss) > 0:
		print(''.join([bases[i-1] for i in poss]))
	else:
		print('invalid')
