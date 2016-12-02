t = int(raw_input())
for u in xrange(t):
	sounds = raw_input().split()
	figured = set()
	while True:
		parts = raw_input().split()
		if len(parts) > 3:
			break
		figured.add(parts[2])
	print ' '.join([s for s in sounds if s not in figured])
