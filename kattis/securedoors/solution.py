n = int(raw_input())

t = set()
for i in xrange(n):
    s = raw_input().split()
    if s[0][1] == 'n':
        #entry
        if s[1] in t:
            print s[1] + ' entered (ANOMALY)'
        else:
            print s[1] + ' entered'
        t.add(s[1])
    else:
        if s[1] in t:
            print s[1] + ' exited'
            t.remove(s[1])
        else:
            print s[1] + ' exited (ANOMALY)'
