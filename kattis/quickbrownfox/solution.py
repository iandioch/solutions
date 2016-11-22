n = int(raw_input())
t = 'abcdefghijklmnopqrstuvwxyz'
for i in xrange(n):
	s = set([c for c in raw_input().lower() if c not in set('0123456789.,?!\'" ')])
	if len(s) == len(t):
		print 'pangram'
	else:
		print 'missing', ''.join([c for c in t if c not in s])
	
