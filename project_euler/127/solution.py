from fractions import gcd

def sieve(n):
    prime_set = []
    is_prime = [True for i in xrange(n)]
    for i in xrange(2, n):
        if is_prime[i]:
            prime_set.append(i)
        for j in xrange(i+i, n, i):
            is_prime[j] = False

    return prime_set

primes = sieve(120000)
prime_set = set(primes)

facts_memo = {}


def prime_facts(n):
    if n in facts_memo:
        return facts_memo[n]

    facts = set()
    for i in xrange(len(primes)):
        if n % primes[i] == 0:
            facts.add(primes[i])
            n = n/primes[i]
            if n <= 1:
                break
            facts.update(prime_facts(n))
            break
    return facts

for i in xrange(120001):
    facts_memo[i] = prime_facts(i)

print 'starting'

def radical(n):
    return reduce(lambda x, y: x*y, prime_facts(n))

radicals = [0 for i in xrange(120001)]
radicals[1] = 1

for i in xrange(2, 120001):
    radicals[i] = radical(i)

def has_no_crossover(a, b):
    for i in a:
        if i in b:
            return False
    return True

def is_coprime(a, b):
    for i in facts_memo[a]:
        if i in facts_memo[b]:
            return False
    return True

c_sum = 0
lim = 120000

for a in xrange(1, lim - 1):
    #a_facts = facts_memo[a]
    for b in xrange(a + 1, lim - a):
        #if not (has_no_crossover(a_facts, facts_memo[b])):
        #    continue
        if gcd(a, b) != 1:
            continue
        if radicals[a] * radicals[b] * radicals[a+b] < a+b:
            print (a, b, a+b)
            c_sum += a+b

print c_sum
