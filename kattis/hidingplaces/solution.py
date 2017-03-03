num_tests = int(input())
for test in range(num_tests):
    g = [[99999999 for y in range(8)] for x in range(8)]
    start = input()
    start_x = ord(start[0])-ord('a')
    start_y = int(start[1]) - 1

    bfs = {(start_x, start_y) : 0}

    def try_to_add(d, x, y):
        if (x, y) in bfs:
            if d < bfs[(x, y)]:
                bfs[(x, y)] = d
        else:
            bfs[(x, y)] = d

    while len(bfs) > 0:
        k = sorted(bfs.keys(), key = lambda x: bfs[x])
        x, y = k[0]
        d = bfs[k[0]]
        del bfs[k[0]]
        if x < 0 or y < 0 or x >= 8 or y >= 8:
            continue
        if g[x][y] > d:
            g[x][y] = d
        else:
            continue
        
        try_to_add(d+1, x+2, y+1)
        try_to_add(d+1, x+2, y-1)
        try_to_add(d+1, x-2, y+1)
        try_to_add(d+1, x-2, y-1)
        try_to_add(d+1, x+1, y+2)
        try_to_add(d+1, x+1, y-2)
        try_to_add(d+1, x-1, y+2)
        try_to_add(d+1, x-1, y-2)
    c = {}
    for x in range(8):
        for y in range(8):
            s = chr(x+ord('a')) + str(y+1)
            d = g[x][y]
            if d in c:
                c[d].append(s)
            else:
                c[d] = [s]

    m = max(c.keys())
    n = sorted(c[m], key=lambda x:x[0])
    n = sorted(n, key=lambda x:x[1], reverse=True)
    print(m, ' '.join(n))
