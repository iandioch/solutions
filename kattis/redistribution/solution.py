n = int(raw_input())

size = [int(x) for x in raw_input().split()]

b = sorted(range(0, n), key = lambda x: -size[x])

if size[b[0]] > sum([size[i] for i in b[1:]]):
	print 'impossible'
else:
	print ' '.join([str(i+1) for i in b])
