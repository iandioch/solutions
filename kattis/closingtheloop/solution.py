num_tests = int(input())
for test in range(1, num_tests+1):
	n = int(input())
	sections = input().split()
	d = {
		'R': [],
		'B': [],
	}
	for section in sections:
		d[section[-1]].append(int(section[:-1]))
	d['R'] = sorted(d['R'], reverse=True)
	d['B'] = sorted(d['B'], reverse=True)
	ir = 0
	ib = 0
	length = 0
	num_rope = 0
	while ir < len(d['R']) and ib < len(d['B']):
		#print('attatching R {} and B {}'.format(d['R'][ir], d['B'][ib]))
		length += d['R'][ir]
		ir += 1
		length += d['B'][ib]
		ib += 1
		num_rope += 2
	print('Case #{}: {}'.format(test, length-num_rope))
