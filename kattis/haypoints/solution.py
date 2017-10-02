m, n = map(int, input().split())
d = {}
for _ in range(m):
	s, v = input().split()
	d[s] = int(v)
for _ in range(n):
	s = None
	ans = 0
	while s != '.':
		s = input()
		for t in s.split():
			if t in d:
				ans += d[t]
	print(ans)
