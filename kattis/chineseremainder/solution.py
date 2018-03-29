def extended_euclidian_algorithm(a, b):
    # https://brilliant.org/wiki/extended-euclidean-algorithm/
    # GCD(a, b) = ax + by. Return GCD(a, b), x, and y.
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b%a
        m, n = x - u*q, y - v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

num = int(input())
for _ in range(num):
    a, n, b, m = map(int, input().split())
    gcd, u, v = extended_euclidian_algorithm(n, m)

    if abs(a-b) % gcd != 0:
        print('no solution')
        continue

    k = (n*m)//gcd # lowest common multiple
    x = ((b-a)*u*n)//gcd + a
    print(x%k, k)
