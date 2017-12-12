import sys

g = [[False for _ in range(1000)] for _ in range(1000)]

for line in sys.stdin.readlines():
    p = line.split()
    if p[0] == 'toggle':
        x, y = map(int, p[1].split(','))
        i, j = map(int, p[-1].split(','))
        for p in range(x, i+1):
            for q in range(y, j+1):
                g[p][q] = not g[p][q]
        continue
    on = (p[1] == 'on')
    x, y = map(int, p[2].split(','))
    i, j = map(int, p[-1].split(','))
    for p in range(x, i+1):
        for q in range(y, j+1):
            g[p][q] = on

ans = 0
for p in range(1000):
    for q in range(1000):
        if g[p][q]:
            ans += 1
print(ans)
