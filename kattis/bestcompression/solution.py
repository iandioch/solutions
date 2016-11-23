a, b = [int(x) for x in raw_input().split()]

maxn = 0
for i in xrange(b+1):
	maxn += 2**i

if maxn >= a:
	print 'yes'
else:
	print 'no'
