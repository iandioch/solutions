"""
Answer is OEIS sequence A002407
The primes are those of the form 3k*(k+1) + 1
"""

primes = []

is_prime = [True for i in xrange(1000000)]
for i in xrange(2, len(is_prime)):
	if is_prime[i]:
		primes.append(i)
		for j in xrange(i+i, len(is_prime), i):
			is_prime[j] = False

prime_set = set(primes)

count = 0

for k in xrange(1, 1000):
	q = k*3*(k+1) + 1
	if q in prime_set:
		count += 1
print count
