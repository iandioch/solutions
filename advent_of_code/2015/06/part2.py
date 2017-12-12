import sys

g = [[0 for _ in range(1000)] for _ in range(1000)]

for line in sys.stdin.readlines():
    p = line.split()
    if p[0] == 'toggle':
        x, y = map(int, p[1].split(','))
        i, j = map(int, p[-1].split(','))
        for p in range(x, i+1):
            for q in range(y, j+1):
                g[p][q] += 2
        continue
    diff = 1
    if p[1] == 'off':
        diff = -1
    x, y = map(int, p[2].split(','))
    i, j = map(int, p[-1].split(','))
    for p in range(x, i+1):
        for q in range(y, j+1):
            g[p][q] = max(0, g[p][q] + diff)

ans = 0
for p in range(1000):
    for q in range(1000):
        if g[p][q]:
            ans += g[p][q]
print(ans)
