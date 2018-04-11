t = int(input())

for _ in range(t):
    n, s = input().strip().split()
    n = int(n)
    m = len(s)
    flip = False
    for _ in range(n):
        d = (m//4)
        if d == 0:
            break
        flip = not flip
        m -= d
        s = s[::-1][:m]
    if flip:
        s = s[::-1]
    print(s)
        
