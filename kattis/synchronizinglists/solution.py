while True:
	n = int(input())
	if n == 0:
		break
	a = [int(input()) for _ in range(n)]
	b = [int(input()) for _ in range(n)]
	sa = sorted(a)
	sb = sorted(b)
	c = list(zip(sa, sb))
	#d = sorted(c, key=lambda x: a.index(x[0]))
	c.sort(key=lambda x: a.index(x[0]))
	print('\n'.join([str(e[1]) for e in c]))
	print()
