from math import factorial

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

n = int(input())
for _ in range(n):
    x = int(input())
    print(nCr(x*2, x) // (x + 1))
