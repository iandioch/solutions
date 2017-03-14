import sys
from math import sqrt

def sq(a):
    x, y = a
    return (x*x - y*y, 2*x*y)

def add(a, b):
    return (a[0] +b[0], a[1] + b[1])

def modulus(a):
    return sqrt(a[0]*a[0] + a[1]*a[1])

casen = 0
for line in sys.stdin.readlines():
    casen += 1
    parts = line.split()
    x = float(parts[0])
    y = float(parts[1])
    r = int(parts[2])
    a = (0,0)
    c = (x,y)
    ok = True
    for _ in range(r):
        b = add(sq(a),c)
        if (modulus(b)) > 2:
            ok = False
        a = b
    if ok:
        print('Case {}: IN'.format(casen))
    else:
        print('Case {}: OUT'.format(casen))
