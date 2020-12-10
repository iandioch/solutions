def rounded(n):
    # Round < 4 down to 0, >= 5 to next 10
    return ((n+5)//10)*10

num_item, num_div = map(int, input().split())
item = list(map(int, input().split()))


sums = [0]*num_item
sums[0] = item[0]
for i in range(1, num_item):
    sums[i] = sums[i-1] + item[i]

dp = [[-1 for _ in range(num_div+1)] for _ in range(num_item+1)]

# Zero items is zero, no matter how many dividers you use.
for i in range(num_div+1):
    dp[0][i] = 0
# Using no dividers, you just pay for all the items. 
for i in range(1, num_item+1):
    dp[i][0] = dp[i-1][0] + item[i-1]

#dp[N][D] = minimal cost of paying for N items using D dividers
for n in range(1, num_item+1):
    for d in range(num_div, 0, -1):
        dp[n][d] = min(dp[n-1][d] + item[n-1], rounded(dp[n-1][d-1] + item[n-1]))

ans = min(rounded(dp[num_item][d]) for d in range(num_div+1))

print(ans)
