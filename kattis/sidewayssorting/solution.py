while True:
	n, d = map(int, input().split())
	if n == d == 0:
		break
	g = [""]*d
	for i in range(n):
		s = input()
		for j in range(d):
			g[j] += (s[j])

	g = sorted(g, key = lambda x: x.lower())
	for i in range(n):
		for j in range(d):
			print(g[j][i], end='')
		print()

