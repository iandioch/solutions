n = int(raw_input())

m = [int(x) for x in raw_input().split()]

ans = {}

for x in xrange(256):
	shifted = x << 1
	if shifted >= 256:
		shifted -= 256;
	y = x^int(shifted)
	ans[y] = x

for y in m:
	print ans[y],
