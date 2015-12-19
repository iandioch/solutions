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

def add_subseq(arr, begin, length):
	seqsum = 0
	for x in xrange(begin, begin+length):
		seqsum += arr[x]
	return seqsum


primes = get_primes(1000000)

prime_set = set()
for prime in primes:
	prime_set.add(prime)

prime_sum = []
prime_sum.append(primes[0])
for prime in primes[1:]:
	prime_sum.append(prime_sum[-1] + prime)

found = False

seq_length = len(primes) - 1

while not found:
	#if seq_length % 100 == 0: print "testing seq length", seq_length
	for begin in xrange(0, len(primes) - 2 - seq_length):
		#seq = primes[begin: begin + seq_length]
		#seqsum = sum(seq)
		#seqsum = add_subseq(primes, begin, seq_length)
		seqsum = prime_sum[begin+seq_length] - prime_sum[begin]
		if seqsum > primes[-1]:
			break
		if seqsum in prime_set:
			print seqsum, seq_length
			found = True

	"""for start in xrange(0, len(primes) - 21):
		index = 0
		seqsum = 0"""
	seq_length -= 1
