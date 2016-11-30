t = int(raw_input())

for tc in xrange(t):
	s = raw_input()
	n = ''
	m = 0
	for i in xrange(len(s)):
		n += s[i]
		bins = bin(int(n))[2:]
		ones = sum([int(x) for x in bins])
		m = max(ones, m)
	print m
