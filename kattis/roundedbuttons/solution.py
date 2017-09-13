import math

def dist(a, b, c, d):
    return math.hypot(d-b, c-a)

n = int(input())
for _ in range(n):
    x, y, w, h, r, m, *c = map(float, input().split())
    m = int(m)
    for i in range(m):
        p = c[i*2]
        q = c[i*2+1]
        inside = False
        if p >= x and p <= x + w and q >= y and q <= y + h:
            if dist(p, q, x+r, y+r) <= r or \
               dist(p, q, x+w-r, y+r) <= r or \
               dist(p, q, x+r, y+h-r) <= r or \
               dist(p, q, x+w-r, y+h-r) <= r or \
               (p >= x+r and p <= x+w-r and q >= y+r and q <= y+h-r) or \
               (p >= x and p <= x+r and q >= y+r and q <= y+h-r) or \
               (p >= x+w-r and p <= x+w and q >= y+r and q <= y+h-r) or \
               (p >= x+r and p <= x+w-r and q >= y and q <= y+r) or \
               (p >= x+r and p <= x+w-r and q >= y+h-r and q <= y+h):
                   inside = True
        if inside:
            print('inside')
        else:
            print('outside')
    print()
