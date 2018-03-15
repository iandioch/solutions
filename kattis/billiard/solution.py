import math
while True:
    a, b, s, m, n = map(int, input().split())
    if a == b == s == n == m == 0:
        break
    x = a*m
    y = b*n
    h = math.hypot(x, y)
    vel = h/s
    angle = math.degrees(math.atan2(y, x))
    print('{:.2f} {:.2f}'.format(angle, vel))
