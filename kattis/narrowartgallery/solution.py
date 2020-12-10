# DP[row number][# blocked][int denoting blocking of prev row] = max possible value
# 0 = nothing blocked
# 1 = left blocked
# 2 = right blocked
num_rows, num_blocked = map(int, input().split())
rows = [tuple(map(int, input().split())) for _ in range(num_rows)]

dp = [[[-1 for _ in range(3)] for _ in range(num_blocked+1)] for _ in range(num_rows)]

# Manually fill in first row
dp[0][0][0] = rows[0][0] + rows[0][1]
if num_blocked > 0:
    dp[0][1][1] = rows[0][1]
    dp[0][1][2] = rows[0][0]

# iterate row number
for i in range(1, num_rows):
    # iterate total rooms blocked so far. We can't have j > i + 1, as we 
    # can only block max one room per row
    for j in range(min(i+1, num_blocked)+1):
        # Case for nothing being blocked on this row
        if max(dp[i-1][j]) >= 0:
            dp[i][j][0] = rows[i][0] + rows[i][1] + max(dp[i-1][j])

        # Try and block either the left or the right...
        if j > 0:
            max_with_left_blocked = max(dp[i-1][j-1][1], dp[i-1][j-1][0])
            if max_with_left_blocked >= 0:
                dp[i][j][1] = rows[i][1] + max_with_left_blocked

            max_with_right_blocked = max(dp[i-1][j-1][2], dp[i-1][j-1][0])
            if max_with_right_blocked >= 0:
                dp[i][j][2] = rows[i][0] + max_with_right_blocked

print(max(dp[-1][num_blocked]))
