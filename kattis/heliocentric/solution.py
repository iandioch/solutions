import sys

t = 1
for line in sys.stdin.readlines():
    e, m = map(int, line.split())
    n = 0
    if e != 0:
        n = 365 - e
        m = (m+n)%687
        e = 0
    while m != 0:
        m = (m+365)%687
        n += 365
    print('Case {}: {}'.format(t, n))
    t += 1
