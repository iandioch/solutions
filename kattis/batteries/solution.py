MAX = 4715
dp = [0, 0]
i = 1
while len(dp) < MAX:
    dp += [i]*i
    i += 1

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n])
