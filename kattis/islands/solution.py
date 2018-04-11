t = int(input())

for _ in range(t):
    ans = 0

    ti, *d = map(int, input().split())
    d = list(d)

    for i in range(1, len(d)-1):
        m = d[i]
        for j in range(i+1, len(d)):
            m = min(m, d[j-1])
            if d[i-1] < m and d[j] < m:
                ans += 1

    print(ti, ans)
