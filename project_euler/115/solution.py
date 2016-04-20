dp = {}

def f(m, n):
	if n in dp:
		return dp[n]
	ans = 1
	for i in xrange(0, n): # i = starting position of the block
		for j in xrange(m, n-i + 1): # j = length of the block
			#print 'putting len', j, 'at pos', i
			ans += f(m, n - i - j - 1)
	dp[n] = ans
	return ans

n = 1
while True:
	if f(50, n) > 1000000:
		break
	n += 1

print n
