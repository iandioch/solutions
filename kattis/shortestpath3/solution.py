INFINITY = 99999999999

while True:
    n, m, q, s = map(int, raw_input().split())
    if n == m == q == s == 0:
        break
    edges = []
    for _ in xrange(m):
        u, v, w = map(int, raw_input().split())
        edges.append((u,v,w))

    # Bellman Ford

    best = [INFINITY for _ in xrange(n)]

    best[s] = 0
    for i in xrange(n):
        for u, v, w in edges:
            if best[u] == INFINITY:
                continue
            if best[u] + w < best[v]:
                best[v] = best[u] + w

    while True:
        nchanged = 0
        for u, v, w in edges:
            if best[v] == -INFINITY:
                continue
            if best[u] == INFINITY:
                continue
            if best[u] + w < best[v]:
                best[v] = -INFINITY
                nchanged += 1
        if nchanged == 0:
            break

    for _ in xrange(q):
        a = int(raw_input())
        b = best[a]
        if b >= INFINITY:
            print('Impossible')
        elif b <= -INFINITY:
            print('-Infinity')
        else:
            print(b)
    print ''
