import sys

g = {}

OPSET = set(['union', 'intersection', 'difference'])

def selection(p):
    if p[0] not in OPSET:
        if p[0] in g:
            return g[p[0]], 1
        else:
            return set([p[0]]), 1

    if p[0] == 'union':
        a, i = selection(p[1:])
        b, j = selection(p[1+i:])
        return a|b, 1+i+j
    elif p[0] == 'intersection':
        a, i = selection(p[1:])
        b, j = selection(p[1+i:])
        return a&b,1+i+j
    elif p[0] == 'difference':
        a, i = selection(p[1:])
        b, j = selection(p[1+i:])
        return a-b,1+i+j

defining = True
for line in sys.stdin.readlines():
    p = line.strip().split()
    if defining and p[0] != 'group':
        defining = False
    if defining:
        _, name, _, *people = p
        g[name] = set(people)
    else:
        a, _ = selection(p)
        print(' '.join(sorted(a)))
