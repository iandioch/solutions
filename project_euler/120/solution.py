ans = 0

for a in xrange(3, 1000+1):
    maxr = 0
    a2 = a*a
    for n in xrange(1, min(5000, a2)):
        x = pow(a-1, n, a2)
        y = pow(a+1, n, a2)
        r = (x+y)%a2
        maxr = max(maxr, r)
    ans += maxr


print ans
