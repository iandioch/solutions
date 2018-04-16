from math import factorial, log

TIMES = [
    lambda n: factorial(n),
    lambda n: 2**n,
    lambda n: n**4,
    lambda n: n**3,
    lambda n: n*n,
    lambda n: n*log(n, 2),
    lambda n: n,
]

MAX = [
    20,
    50,
    200,
    2000,
    32000,
    10**8,
    10**10
]

m, n, p = map(int, input().split())
if n >= MAX[p-1] or TIMES[p-1](n) > m:
    print('TLE')
else:
    print('AC')
