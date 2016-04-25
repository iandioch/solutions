import sys

is_prime = [True for i in xrange(8000000)]
primes = []

for i in xrange(2, len(is_prime)):
    if is_prime[i]: 
        primes.append(i)
        for j in xrange(i+i, len(is_prime), i):
            is_prime[j] = False

prime_facts = {}
for p in primes[:500500]:
    prime_facts[p] = 1

prime_facts[2] = 2 # maps a prime p to the highest y used so far, where y = p^x for some x

n = 2 # the current number
i = 1 # the current iteration
mod = 500500507
next_prime_index = 1

while i < 500500:
    q = sys.maxint # the number to mult by to double the number of factors
    base_q = sys.maxint # x when q = x^y

    for p in xrange(next_prime_index):
        prime = primes[p]
        k = prime_facts[prime]*prime_facts[prime]
        if k < q:
            q = k
            base_q = prime
        elif prime_facts[prime] == prime:
            break

    if primes[next_prime_index] < q:
        q = primes[next_prime_index]
        base_q = q
        next_prime_index += 1

    n = (n*(q%mod))%mod

    prime_facts[base_q] = q
    i += 1

print n
