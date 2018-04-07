import heapq

from collections import defaultdict

while True:
    n, m, qu, s = map(int, input().split())
    if n == m == qu == s == 0:
        break
    d = defaultdict(list)
    best = {}
    for _ in range(m):
        u, v, t, p, w = map(int, input().split())
        d[u].append((v, t, p, w))
    q = []
    heapq.heappush(q, (0, s))
    while len(best) < n and len(q):
        cost, curr = heapq.heappop(q)
        if curr in best and best[curr] <= cost:
            continue
        best[curr] = cost
        for other, t, p, w in d[curr]:
            nt = cost 
            if cost < t:
                nt = t
            elif p == 0:
                if cost != t:
                    continue
            elif (cost - t) % p != 0:
                r = p - ((cost - t) % p)
                nt = cost + r
            if other in best and best[other] <= nt:
                continue
            heapq.heappush(q, (nt + w, other))
    for _ in range(qu):
        a = int(input())
        if a not in best:
            print('Impossible')
            continue
        print(best[a])
    print()

