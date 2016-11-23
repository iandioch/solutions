def base_10_to_n(num, chardict):
	a = ''
	n = len(chardict)
	curr = num
	while curr > 0:
		remainder = curr % n
		a = chardict[remainder] + a
		curr /= n
	return a

def base_n_to_10(num, chardict):
	n = 0
	for i in xrange(len(num)):
		n = len(chardict)*n + chardict.index(num[i])
	return n

n = int(raw_input())
for i in xrange(n):
	parts = raw_input().split()
	print 'Case #%d: %s' % ((i+1), base_10_to_n(base_n_to_10(parts[0], parts[1]), parts[2]))

