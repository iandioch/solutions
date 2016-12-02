n = int(raw_input())

c = sorted([int(raw_input()) for i in xrange(n)], reverse=True)
tot = 0

i = 0
while i + 2 < len(c):
	tot += c[i] + c[i+1]
	i += 3

while i < len(c):
	tot += c[i]
	i += 1

print tot
