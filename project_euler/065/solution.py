def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a, b):
    return (a*b)//gcd(a, b)

def flip_fraction(numerator, denom_fract):
    return (numerator * denom_fract[1], denom_fract[0])

def simplify(f):
    d = gcd(f[0], f[1])
    return (f[0]//d, f[1]//d)

def add_fraction(a, b):
    if a[0] == 0:
        return b
    if b[0] == 0:
        return a
    denom = lcm(a[1], b[1])
    an = (a[0] * (denom//a[1]))
    bn = (b[0] * (denom//b[1]))
    return simplify((an+bn,denom)) 

def nth_convergent(n):
    # 0 : 1
    # 1: 2
    # 2: 1
    # 3: 1
    if (n % 3) == 1:
        return (1 + n//3)*2
    return 1

def recur(j, n):
    if j > n:
        return (0, 0)
    basis = nth_convergent(j)
    under = recur(j+1, n)
    denom = add_fraction((basis, 1), under)
    flipped = flip_fraction(1, denom)
    tot = flipped
    #print(f'recur({j}, {n}): {basis} + {under} (flipped = {flipped})')
    return tot

def nth_in_series(n):
    basis = (2, 1)
    if n == 0:
        return basis
    return add_fraction(basis, recur(0, n-1))

# above is 0-indexed, so we take the 99th item
d = sum(int(d) for d in str(nth_in_series(99)[0]))
print(d)
