from decimal import *
from fractions import Fraction

getcontext().prec = 115

def count_digs(n):
    s = str(n)

    if '.' not in s:
        # must be perfect square
        return 0

    s = list(s)
    del s[s.index('.')]

    return sum([int(i) for i in s[:100]]) 

tot = 0
for i in xrange(2, 100):
    n = Decimal(i).sqrt()
    tot += count_digs(n) 
print tot

