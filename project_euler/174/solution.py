num = 0
limit = 10000000
max_tiles = 1000000


count = {}

max_n = 15


for x in xrange(3, limit):
    # x is the length of one side
    tot = x*x
    start = 2 if x % 2 == 0 else 1
    for y in xrange(x-2, start-1, -2):
        # y is the length of the inner square
        v = tot - y*y
        # v is the number of tiles used
        if v > max_tiles:
            break
        
        if v in count:
            count[v] += 1
        else:
            count[v] = 1
        #print x, y, 'using', tot - y*y, 'tiles'

L = {}
for i in count:
    if count[i] in L:
        L[count[i]] += 1
    else:
        L[count[i]] = 1

print sum([L[i] for i in xrange(11) if i in L])
