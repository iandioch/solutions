from math import sin, cos

p, a, b, c, d, n = map(int, input().split())

def price(k):
    return p*(sin(a*k + b) + cos(c*k + d) + 2)

biggest_drop = 0
maxx = 0
for ni in range(1, n+1):
    v = price(ni)
    maxx = max(v, maxx)
    biggest_drop = max(maxx - v, biggest_drop)

print(biggest_drop)
