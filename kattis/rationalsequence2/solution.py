num_tests = int(input())
for test in range(1, num_tests+1):
	k, frac = input().split()
	p, q = map(int, frac.split('/'))
	num, denom = p, q
	seq = []
	while not (num == 1 and denom == 1):
		if num > denom:
			# is on RHS of parent
			num -= denom
			seq.append("1")
		else:
			# is on LHS of parent
			denom -= num
			seq.append("0")
	seq.append('1')
	print(k, int(''.join(seq[::-1]), base=2))
	
