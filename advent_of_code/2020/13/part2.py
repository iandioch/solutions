from functools import reduce
import operator

def main():
    target = int(input())
    bus = [None if c == 'x' else int(c) for c in input().split(',')]

    # We want to find some t such that:
    # t % bus[0] = 0
    # (t+1) % bus[1] = 0
    # (t+2) % bus[2] = 0
    # etc.
    #
    # First, remove any i for which bus[i] is None ('x' in the input).
    #
    # This leaves something like:
    # t % bus[0] = 0
    # (t+2) % bus[2] = 0
    # (t+10) % bus[10] = 0
    #
    # This is ~equivalent to (this looks more like the mathematical notation):
    # t == 0            mod bus[0]
    #   ...
    # t == (bus[i]-i)   mod bus[i]
    # (with an extra step to make sure the subtraction doesn't cause any nums to
    # go negative, etc.)
    # 
    # This is a case of the Chinese Remainder Theorem (CRT), which came up in
    # Project Euler once upon a time iirc. If we call the 't' above X instead,
    # call 'bus[i]' N_i, and call '(bus[i]-i)' A_i, it gives us:
    # x == A_i    (mod N_i)
    # This statement is the exact case in the CRT. However, to solve the CRT,
    # N should only contain coprimes. We'll also need the "modular inverse" func
    # (= extended Euclidian algorithm, something something Bezout's identity),
    # which I don't understand.

    n = [b for b in bus if b is not None]
    a = [(bus[i] - i) for i in range(len(bus)) if bus[i] is not None]
    for i in range(len(a)):
        # Fix negatives and a[i] and the like.
        a[i] %= n[i]

    def mod_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a%b
            x0, x1 = x1 - q*x0, x0
        if x1 < 0:
            x1 += b0
        return x1

    def chinese_remainder_theorem(a, n):
        N = reduce(operator.mul, n)
        tot = 0
        for n_i, a_i in zip(n, a):
            p = N // n_i
            tot += a_i * mod_inv(p, n_i) * p
        return tot % N

    print(chinese_remainder_theorem(a, n))

main()
