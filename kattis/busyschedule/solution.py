while True:
    n = int(input())
    if n == 0:
        break
    d = []
    for _ in range(n):
        p = input().split()
        t = p[0].split(':')
        if t[0] == '12':
            t[0] = '0'
        d.append((p[1], int(t[0]), int(t[1])))
    d.sort()
    for e in d:
        h = e[1]
        m = e[2]
        am = e[0]
        hs = str(h)
        if h == 0:
            hs = '12'
        ms = str(m)
        if len(ms) == 1:
            ms = '0' + ms
        print('{}:{} {}'.format(hs, ms, e[0]))
    print()
