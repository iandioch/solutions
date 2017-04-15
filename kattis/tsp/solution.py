def dist(pa, pb):
    return (pa[0]-pb[0])**2 + (pa[1]-pb[1])**2

n = int(input())

p = []

for i in range(n):
    px, py = map(float, input().split())
    p.append((px, py))

tour = []
used = [False for _ in range(n)]

tour.append(0)
used[0] = True

for i in range(1, n):
    best = -1
    for j in range(0, n):
        t = p[tour[i-1]]
        if not used[j] and (best == -1 or dist(t, p[j]) < dist(t, p[best])):
            best = j
    tour.append(best)
    used[best] = True

print('\n'.join(str(v) for v in tour))
