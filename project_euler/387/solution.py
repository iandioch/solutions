import sys

def count_digits(n):
    return sum([int(c) for c in str(n)])

harshads = set() # right-truncatable harshad numbers

def is_harshad(n):
    if n < 10:
        return True
    a = (n % count_digits(n) == 0) and is_harshad(n//10)
    return a

# worth looking into a better prime check
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

limit = 10**14
ans = 0

for i in xrange(0, 10):
    harshads.add(i)

for i in xrange(2, 14):
    w = set()
    for j in harshads:
        w.add(j*10)
        for i in xrange(1, 10):
            k = j*10 + i
            if is_harshad(k):
                w.add(k)
    harshads = w

harshads.remove(0)
for j in harshads:
    p = is_prime(j//count_digits(j))
    if not p:
        continue
    for i in [1, 3, 7, 9]:
        k = j*10 + i
        if is_prime(k):
            ans += k
             
print ans
