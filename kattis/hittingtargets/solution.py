import math

rects = []
circles = []

num_target = int(input())
for _ in range(num_target):
    s = input().split()
    if s[0][0] == 'r':
        # rectangle
        rects.append(list(map(int, s[1:])))
    else:
        # circle
        circles.append(list(map(int, s[1:])))

num_shot = int(input())
for _ in range(num_shot):
    x, y = map(int, input().split())
    n = 0
    for blx, bly, urx, ury in rects:
        if x >= blx and x <= urx and y >= bly and y <= ury:
            n += 1
    for cx, cy, r in circles:
        d = math.sqrt((cy-y)**2 + (cx-x)**2)
        if d <= r:
            n += 1
    print(n)
