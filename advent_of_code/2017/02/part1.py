import sys

d = []
for line in sys.stdin.readlines():
	v = list(map(int, line.strip().split()))
	d.append(max(v) - min(v))

print(sum(d))
