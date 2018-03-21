from itertools import permutations

def is_prime(digs):
    n = 0
    for d in digs:
        n *= 10
        n += d
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return n >= 2

n = int(input())
for _ in range(n):
    s = [int(c) for c in input().strip()]
    ans = 0
    d = set()
    for length in range(1, len(s)+1):
        for p in permutations(s, length):
            if p[0] == 0:
                continue
            if p not in d and is_prime(p):
                ans += 1
            d.add(p)
    print(ans)
