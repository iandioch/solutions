import sys

digs = { 
    """**** ** ** ****""": 0,
    """  *  *  *  *  *""": 1,
    """***  *****  ***""": 2,
    """***  ****  ****""": 3,
    """* ** ****  *  *""": 4,
    """****  ***  ****""": 5,
    """****  **** ****""": 6,
    """***  *  *  *  *""": 7,
    """**** ***** ****""": 8,
    """**** ****  ****""": 9
}

lines = sys.stdin.readlines()

num = len(lines[0])//4

valid = True
n = 0

for i in xrange(num):
    r = [(t[i*4:i*4+3]) for t in lines]
    s = ''.join(r)
    if s in digs:
        n *= 10
        n += digs[s]
    else:
        valid = False
        break

if valid and n % 6 == 0:
    print 'BEER!!'
else:
    print 'BOOM!!'
