while True:
    p = list(map(int, input().split()))
    if len(p) == 1:
        break
    c = p[1]
    k = set(map(int, input().split()))
    ok = True
    for _ in range(c):
        tot = 0
        _, req, *v = map(int, input().split())
        for j in v:
            if j in k:
                tot += 1
        ok = ok and tot >= req
    if ok:
        print('yes')
    else:
        print('no')
