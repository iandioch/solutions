dp = {}

def f(n):
	if n in dp:
		return dp[n]
	ans = 1
	for i in xrange(0, n): # i = starting position of the block
		for j in xrange(2, min(5, n-i+1)): # j = length of the block
			#print 'putting len', j, 'at pos', i, 'in total len', n
			ans += f(n - i - j)
	dp[n] = ans
	return ans

print f(5)
print f(50)
