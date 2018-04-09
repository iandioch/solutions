while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    rx, ry = 0, 0
    px, py = 0, 0
    n = int(input())
    for _ in range(n):
        c, d = input().split()
        d = int(d)
        if c == 'u':
            py += d
            ry = min(h-1, ry+d)
        elif c == 'r':
            px += d
            rx = min(w-1, rx+d)
        elif c == 'd':
            py -= d
            ry = max(0, ry-d)
        elif c == 'l':
            px -= d
            rx = max(0, rx-d)
    print('Robot thinks', px, py)
    print('Actually at', rx, ry)
    print()
