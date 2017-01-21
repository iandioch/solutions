while True:
    n = int(raw_input())
    if n == 0:
        break
    d = {}
    for i in xrange(n):
        parts = raw_input().split()
        for p in parts[1:]:
            if p in d:
                d[p].add(parts[0])
            else:
                d[p] = set()
                d[p].add(parts[0])


    for k in sorted(d):
        print k, ' '.join(sorted(d[k]))
    print ''
