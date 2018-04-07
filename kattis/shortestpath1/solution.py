import heapq

from collections import defaultdict

while True:
    n, m, qu, s = map(int, input().split())
    if n == m == qu == s == 0:
        break
    d = defaultdict(list)
    best = {}
    for _ in range(m):
        u, v, w = map(int, input().split())
        d[u].append((v, w))
    q = []
    heapq.heappush(q, (0, s))
    while len(best) < n and len(q):
        cost, curr = heapq.heappop(q)
        if curr in best and best[curr] <= cost:
            continue
        best[curr] = cost
        for other, w in d[curr]:
            if other in best and best[other] <= cost + w:
                continue
            heapq.heappush(q, (cost + w, other))
    for _ in range(qu):
        a = int(input())
        if a not in best:
            print('Impossible')
            continue
        print(best[a])
    print()

