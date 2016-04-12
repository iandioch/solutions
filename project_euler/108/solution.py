limit = 1000000
num_facts = [0 for i in xrange(limit)]

def sieve(n):
    primes = []
    for i in xrange(2, n):
        if num_facts[i] == 0:
            primes.append(i)
        for j in xrange(i+i, n, i):
            num_facts[j] += 1
    return primes

sieve(limit)
dic = {i:num_facts[i] for i in xrange(limit)}
prio = sorted(dic.keys(), key = lambda x : x)
prio = sorted(prio, key = lambda x: dic[x], reverse=True)

count = [0 for i in xrange(limit)]

print 'iterating'
curr_min = limit+1

for n in prio:
    c = 0
    if n > curr_min:
        continue
    for x in xrange(n+1, 2*n+2):
        y = (-n*x)/(n-x)
        if y*(n-x) == (-n*x):
            #print n, x, y
            c += 1
            count[n] += 1
            if c > 1000:
                #print n, c
                curr_min = min(curr_min, n)
                print 'min:', curr_min
                break
    if c < 500:
        break
