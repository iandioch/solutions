t = int(raw_input())

for u in xrange(1, t+1):
	n = [int(x) for x in raw_input().split()][1:]
	d = {}
	print 'Case #%d:' % u
	found = False
	for i in n:
		news = {}
		for j in d:
			if i+j in d:
				found = True
				print ' '.join([str(x) for x in d[j+i]])
				print ' '.join([str(x) for x in (d[j] + [i])])
				break
			news[j+i] = d[j] + [i] # could be optimised w linkedlist
		if found:
			break
		if i in d:
			print ' '.join([str(x) for x in d[i]])
			print i
			found = True
			break
		for k in news:
			d[k] = news[k]
		d[i] = [i]
				
	if not found:
		print 'Impossible'
