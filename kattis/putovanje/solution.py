n, c = map(int, input().split())
f = list(map(int, input().split()))
b = 0
for i in range(len(f)):
    t = 0
    m = 0
    for j in range(i, len(f)):
        if t + f[j] <= c:
            t += f[j]
            m += 1
    b = max(b, m)
print(b)
