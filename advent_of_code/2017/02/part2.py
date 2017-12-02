import sys

d = []
for line in sys.stdin.readlines():
	v = list(map(int, line.strip().split()))
	ok = False
	for i in range(0, len(v)-1):
		for j in range(i+1, len(v)):
			if v[i] % v[j] == 0:
				d.append(v[i]//v[j])
				ok = True
				break
			elif v[j] % v[i] == 0:
				d.append(v[j]//v[i])
				ok = True
				break
		if ok:
			break
print(sum(d))
