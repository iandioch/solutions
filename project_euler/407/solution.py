from math import sqrt
from itertools import combinations

# same method as described here: http://codereview.stackexchange.com/a/25943
# takes ~ 4 and a quarter mins
# compiled language might speed it up a lot I think

maxnum = 10**7 + 1

prime_powers = set()
prime_factors = [[] for i in xrange(maxnum)]
totient = [i for i in xrange(maxnum)]

# sieve to get the prime factors of each number
# and get the totients while we're at it
for i in xrange(2, maxnum):
    if len(prime_factors[i]) == 0:
        totient[i] = i - 1
        for j in xrange(i+i, maxnum, i):
            highest_pow = 1
            t = j

            while t % i == 0:
                t = t / i
                highest_pow *= i
            prime_factors[j].append(highest_pow)
            totient[j] = (totient[j] * (i-1))//i

        # keep a set of the numbers that are a perfect prime power handy
        k = 1
        while i**k < maxnum:
            prime_powers.add(i**k)
            k += 1

total = 0

for n in xrange(2, maxnum):
    if n in prime_powers:
        # all prime powers give an answer of 1
        # I noticed this by observation, then it made sense
        # as for a*a == a (mod n), n must divide a*a evenly
        # this will never be true when a is prime
        total += 1
        continue

    facts = prime_factors[n]
    best = 1
    for i in xrange(1, len(facts)):
        # get all the combinations of the factors
        for comb in combinations(facts, i):
            # use the combination to get the two (potenitally) composite factors p*q = n
            p = reduce(lambda x, y:x*y, comb)
            q = n / p
            # p divides a; q divides (a - 1)
            # a = pr
            # pr == 1 (mod q), almost by definition of p and q
            # therefore r = 1/q (mod q)
            # get 1/q from Euler's theorem:
            # https://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Using_Euler.27s_theorem
            best = max(best, p*pow(p, totient[q] - 1, q))

    total += best

print total
             
        
# number theory is mad

