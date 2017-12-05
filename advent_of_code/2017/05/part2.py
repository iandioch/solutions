import sys

g = list(map(int, sys.stdin.readlines()))
i = 0
count = 0

while i >= 0 and i < len(g):
	j = i + g[i]
	if g[i] >= 3:
		g[i] -= 1
	else:
		g[i] += 1
	i = j
	count += 1

print(count)
