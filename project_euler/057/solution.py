n = 3
d = 2
old_n = 3


num = 0

for i in xrange(1, 1000):
    n = old_n + 2*d

    d = d + old_n

    old_n = n
    if len(str(n)) > len(str(d)):
        num += 1

print num
