n = int(input())
for _ in range(n):
    x, t = input().split()
    x = int(x)
    t = float(t)
    print((x-1)*60/t, x*60/t, (x+1)*60/t)
