import math

def dist_point_line(x, a1, a2):
    if a1 == a2:
        # "line" is actually just a point
        return math.hypot(x[0] - a1[0], x[1] - a1[1])
    dx = a2[0] - a1[0]
    dy = a2[1] - a1[1]

    t = ((x[0] - a1[0])*dx + (x[1] - a1[1])*dy) / (dx**2 + dy**2)
    if t < 0:
        return math.hypot(x[0] - a1[0], x[1] - a1[1])
    elif t > 1:
        return math.hypot(x[0] - a2[0], x[1] - a2[1])
    else:
        # 0 <= t <= 1
        nx = a1[0] + t*dx
        ny = a1[1] + t*dy
        return math.hypot(x[0] - nx, x[1] - ny)
    

def intersect(a1, a2, b1, b2):
    dx1 = a2[0] - a1[0]
    dy1 = a2[1] - a1[1]
    dx2 = b2[0] - b1[0]
    dy2 = b2[1] - b1[1]

    d = dx2 * dy1 - dy2 * dx1
    if d == 0:
        return False
    s = (dx1 * (b1[1] - a1[1]) + dy1 * (a1[0] - b1[0])) / d
    t = (dx2 * (a1[1] - b1[1]) + dy2 * (b1[0] - a1[0])) / (-d)
    return (0 <= s < 1) and (0 <= t <= 1)

def min_dist(a1, a2, b1, b2):
    if intersect(a1, a2, b1, b2):
        return 0
    return min(dist_point_line(a1, b1, b2),
               dist_point_line(a2, b1, b2),
               dist_point_line(b1, a1, a2),
               dist_point_line(b2, a1, a2))

n = int(input())
for _ in range(n):
    p = list(map(int, input().split()))
    a1 = (p[0], p[1])
    a2 = (p[2], p[3])
    b1 = (p[4], p[5])
    b2 = (p[6], p[7])
    print('{:.2f}'.format(min_dist(a1, a2, b1, b2)))
