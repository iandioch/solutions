primes = []
is_prime = [True for x in xrange(500000)]
for i in xrange(2, len(is_prime)):
    if is_prime[i]:
        primes.append(i)
        for j in xrange(i+i, len(is_prime), i):
            is_prime[j] = False

target = 10**10

for n in xrange(0, len(primes), 2):
    maxr = 0
    p = primes[n]
    r = 2*p*n

    if r > target:
        print n+1
        break
