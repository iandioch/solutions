dp = {}

def count(n):
	if n in dp:
		return dp[n]
	ans = 1
	for i in xrange(0, n): # i = starting position of the block
		for j in xrange(3, n-i + 1): # j = length of the block
			#print 'putting len', j, 'at pos', i
			ans += count(n - i - j - 1)
	dp[n] = ans
	return ans

print count(50)
