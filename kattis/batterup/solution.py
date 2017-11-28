n = int(input())
s = map(int, input().split())

v = []
for m in s:
	if m >= 0:
		v.append(m)

print(sum(v)/len(v))
