def sieve(n):
    is_prime = [True for i in xrange(n)]
    primes = []
    for i in xrange(2, n):
        if is_prime[i]:
            primes.append(i)
        for j in xrange(i+i, n, i):
            is_prime[j] = False
    return primes

dp = {}

lim = 100000
primes = sieve(lim+1)

def prime_fact(n):
    if n in dp:
        return dp[n]
    fact = set()
    for p in primes:
        if n % p == 0:
            fact.add(p)
            if n <= 1:
                break
            fact.update(prime_fact(n/p))
            break
    dp[n] = fact
    return fact

def rad(n):
    return reduce(lambda x, y: x*y, prime_fact(n))

rads = {1:1}
for i in xrange(2, lim+1):
    rads[i] = rad(i)

s_rads = sorted(rads, key = lambda x: rads[x])
for r in s_rads:
    print r, rads[r]
print s_rads[9999]
