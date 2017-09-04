h, w = map(int, input().split())
g = []
for _ in range(h):
    g.append(input())

v = [0]*5
for i in range(0, w-1):
    for j in range(0, h-1):
        a = g[j][i]
        b = g[j+1][i]
        c = g[j][i+1]
        d = g[j+1][i+1]
        if a == '#' or b == '#' or c == '#' or d == '#':
            continue
        n = 0
        if a == 'X':
            n += 1
        if b == 'X':
            n += 1
        if c == 'X':
            n += 1
        if d == 'X':
            n += 1
        v[n] += 1

for i in range(5):
    print(v[i])
