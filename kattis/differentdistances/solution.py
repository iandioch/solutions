while True:
    s = input().split()
    if len(s) == 1:
        break
    x1, y1, x2, y2, p = map(float, s)
    a = (abs(x1-x2)**p + abs(y1-y2)**p)**(1/p)
    print('{:.8f}'.format(a))
