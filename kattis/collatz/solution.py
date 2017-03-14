while True:
    a, b = map(int, input().split())
    ao = a
    bo = b
    if a == 0 and b == 0:
        break
    ad = {}
    an = 0
    while True:
        ad[a] = an
        an += 1
        if a == 1:
            break
        if a % 2 == 0:
            a //= 2
        else:
            a = 3*a + 1
    bn = 0
    while b not in ad:
        if b % 2 == 0:
            b //= 2
        else:
            b = 3*b + 1
        bn += 1
    print ('{} needs {} steps, {} needs {} steps, they meet at {}'.format(
                ao, ad[b], bo, bn, b))
