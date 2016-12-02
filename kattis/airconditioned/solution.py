n = int(raw_input())

ms = []
for i in xrange(n):
	s = raw_input().split()
	m = (int(s[0]), int(s[1]))
	ms.append(m)

ms = sorted(ms, key=lambda x: x[1])

ans = 0
while len(ms):
	ans += 1
	t = ms[0][1]
	x = 0
	while x < len(ms) and (ms[x][0] <= t <= ms[x][1]):
		x += 1
	ms = ms[x:]
print ans
