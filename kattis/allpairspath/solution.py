INFINITY = 99999999999

while True:
    n, m, q = map(int, raw_input().split())
    if n == m == q == 0:
        break

    edges = []
    dist = [[INFINITY for _ in xrange(n)] for _ in xrange(n)]
    for _ in xrange(m):
        u, v, w = map(int, raw_input().split())
        dist[u][v] = min(w, dist[u][v])

    for i in xrange(n):
        dist[i][i] = 0

    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if dist[i][k] >= INFINITY or dist[k][j] >= INFINITY:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if dist[j][j] < 0 and dist[k][j] < INFINITY and dist[j][i] < INFINITY:
                    dist[k][i] = -INFINITY

    for _ in xrange(q):
        a, b = map(int, raw_input().split())
        c = dist[a][b]
        if c <= -INFINITY:
            print('-Infinity')
        elif c >= INFINITY:
            print('Impossible')
        else:
            print(c)
    print ''
