num = 0
limit = 10000000
max_tiles = 1000000


for x in xrange(3, limit):
    # x is the length of one side
    tot = x*x
    start = 2 if x % 2 == 0 else 1
    for y in xrange(x-2, start-1, -2):
        if tot - y*y > max_tiles:
            break
        num += 1 
        #print x, y, 'using', tot - y*y, 'tiles'

print num
