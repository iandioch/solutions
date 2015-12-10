def sum_divisors(n):
	r = 0
	for x in xrange(1, n):
		if n % x == 0:
			r += x
	return r

dp = []
for x in xrange(20000):
	dp.append(sum_divisors(x))

print "checking nums"
total = 0

for x in xrange(1,10001):
	if dp[x] < len(dp):
		if x == dp[dp[x]] and x != dp[x]:
			print x,dp[x]
			total += x
	elif x == sum_divisors(dp[x]) and x != dp[x]:
		print x,dp[x]
		total += x

print total
