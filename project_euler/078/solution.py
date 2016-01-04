import math

p = {}

# euler generating function to get the partition numbers
# see http://mathworld.wolfram.com/PartitionFunctionP.html
# followed tips by harpanet and optimisation by snq from thread of project euler #76
def getP(n):
	if n < 0:
		return 0
	n = int(n)
	if(n in p):
		return p[n]

	c = 0

	k = 1
	while k*k <=n :
		pn1 = getP(n - (3*k - 1)*k/2)
		pn2 = getP(n - (3*k + 1)*k/2)
		if k % 2 == 1:
			c += pn1 + pn2
		else:
			c -= pn1 + pn2
		k += 1
	p[n] = c
	return c



def main():
	p[0] = 1
	p[1] = 1
	p[2] = 2
	p[3] = 3
	p[4] = 5
	p[5] = 7
	p[6] = 11
	p[7] = 15
	p[8] = 22
	p[9] = 30
	p[10] = 42
	for i in xrange(500, 100000):
		#print i, getP(i)
		if getP(i) % 1000000 == 0:
			print i
			return

if __name__ == "__main__":
	main()