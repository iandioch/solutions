a, b = [int(x) for x in raw_input().split()]

booked = set()
for i in xrange(b):
	n = int(raw_input())
	booked.add(n)

found = False
for i in xrange(1, a+1):
	if i not in booked:
		print i
		found = True
		break

if not found:
	print 'too late'
