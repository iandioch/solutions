def get_primes(N):
	arr = []
	nums = [False] * N
	for x in xrange(2,N):
		if(not nums[x]):
			arr.append(x)
			y = x
			while y < len(nums):
				nums[y] = True
				y += x
	return arr


def go():
	prime_list = get_primes(1000000)
	primes = set()
	for prime in prime_list:
		primes.add(prime)

	maxn = 0

	for a in xrange(-1000, 1001):
		for b in xrange(-1000, 1001):
			n = -1
			loop = True
			while loop:
				n += 1
				x = n*(n+a) + b
				if x not in primes:
					loop = False

			if n > maxn:
				maxn = n
				print a, b, n, a*b


if __name__ == "__main__":
	go()
