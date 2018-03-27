import math

t = int(input())
for _ in range(t):
    n = int(input())
    splat = []
    for _ in range(n):
        x, y, vol, colour = input().split()
        x, y = float(x), float(y)
        vol = float(vol)
        radius = math.sqrt(vol/math.pi)
        splat.append((x, y, radius, colour))
    splat = splat[::-1]
    m = int(input())
    for _ in range(m):
        i, j = map(float, input().split())
        ok = False
        for x,y,r,colour in splat:
            if abs(x-i) > r and abs(y-j) > r:
                continue
            d = math.sqrt((x-i)**2 + (y-j)**2)
            if d < r:
                ok = True
                print(colour)
                break
        if not ok:
            print('white')
