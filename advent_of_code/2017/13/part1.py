import sys

d = {}
for line in sys.stdin.readlines():
    p = line.split(':')
    d[int(p[0])] = int(p[1])

c = {i:0 for i in d}
ans = 0
end = max(d.keys()) + 1

for curr in range(end):
    for e in d:
        p = c[e]
        if p >= d[e]:
            p = d[e] * 2 - 2 - p
        if curr == e and p == 0:
            ans += d[e]*curr
        c[e] += 1
        if c[e] >= d[e] * 2 - 2:
            c[e] = 0
print(ans)
