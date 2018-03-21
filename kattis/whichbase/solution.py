n = int(input())
for _ in range(n):
    a, v = input().split()
    x, y, z = 0, 0, 0
    try:
        x = int(v, 8)
    except:
        pass
    try:
        y = int(v)
    except:
        pass
    try:
        z = int(v, 16)
    except:
        pass
    print(a, x, y, z)
