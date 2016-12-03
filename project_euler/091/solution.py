from fractions import gcd

n = 50

# num with two edges of triangle on edges of graph 
ans = n*n*3

# num with one edge of triangle on edge of graph
for x in xrange(1, n+1):
	for y in xrange(1, n+1):
		mov = gcd(x,y)
		a = (y*mov)/x
		b = ((n-x)*mov)//y
		ans += min(a, b)*2

print ans
