import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

t = int(input())
for _ in range(t):
    x, y = map(float, input().split())
    n = int(input())
    ok = False
    for _ in range(n):
        i, j = map(float, input().split())
        if ok:
            continue
        ok = (dist(x, y, i, j) <= 8)
    print('light a candle' if ok else 'curse the darkness')
