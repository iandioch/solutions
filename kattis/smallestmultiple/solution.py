import functools
import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a*b//gcd(a, b)

for line in sys.stdin.readlines():
    print(functools.reduce(lcm, map(int, line.split())))
