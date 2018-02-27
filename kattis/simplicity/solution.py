s = input().strip()

d = {}
for c in s:
    d[c] = s.count(c)

e = sorted(d, key=lambda x:d[x])
tot = 0
i = 0
while len(e[i:]) > 2:
    tot += d[e[i]]
    i += 1

print(tot)
