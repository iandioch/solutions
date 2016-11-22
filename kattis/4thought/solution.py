possibilities = ['4']

for i in xrange(3):
	ns = []
	for s in possibilities:
		ns.append(s+' * 4')
		ns.append(s+' + 4')
		ns.append(s+' - 4')
		ns.append(s+' / 4')
	possibilities = ns

solutions = {}
for p in possibilities:
	a = eval(p)
	solutions[a] = p

tests = int(raw_input())
for i in xrange(tests):
	n = int(raw_input())
	if n in solutions:
		s = solutions[n]
		print s, '=', n
		#print '4', s[0], '4', s[1], '4', s[2], '4 =', n
	else:
		print('no solution')
