p = list(map(int, input().split()))
q = sorted(p)
while True:
    if p[0] > p[1]:
        p[0], p[1] = p[1], p[0]
        print(' '.join(map(str, p)))
    if p[1] > p[2]:
        p[1], p[2] = p[2], p[1]
        print(' '.join(map(str, p)))
    if p[2] > p[3]:
        p[2], p[3] = p[3], p[2]
        print(' '.join(map(str, p)))
    if p[3] > p[4]:
        p[3], p[4] = p[4], p[3]
        print(' '.join(map(str, p)))
    if p == q:
        break
