primes = []
is_prime = [True for i in xrange(1000000)]

for i in xrange(2, len(is_prime)):
    if is_prime[i]:
        primes.append(i)
        for j in xrange(i+i, len(is_prime), i):
            is_prime[j] = False

def get_next_row(p):
    q = [1] + [p[i] + p[i+1] for i in xrange(len(p)-1)] + [1]
    return q

def is_square_free(n):

    if n % 4 == 0:
        return False
    for p in primes:
        q = p*p
        if q > n:
            break
        if n % q == 0:
            return False
    return True

s = [1]

n = set()
for i in xrange(1, 51):
    t = get_next_row(s)
    n.update(t)
    s = t


print sum([i for i in n if is_square_free(i)])
