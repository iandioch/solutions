n = int(input())
d = list(map(int, input().split()))

dp = [[0 for _ in range(2*n)] for _ in range(2*n)]
for v in range(n):
    ans = d[v]%2
    dp[v][v] = ans
    dp[v+n][v+n] = ans

for c in range(2, n+1):
    for a in range(2*n):
        b = a + c - 1
        if b >= 2*n:
            break
        dp[a][b] = max(dp[a][a] - dp[a+1][b], dp[b][b] - dp[a][b-1])

ans = 0
for i in range(n):
    if dp[i][i] > dp[i+1][i+n-1]:
        ans += 1

print(ans)
