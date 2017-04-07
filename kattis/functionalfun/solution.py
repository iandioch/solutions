import sys

lines = sys.stdin.readlines()
line = 0

while line < len(lines):
    domain = lines[line].split()[1:]
    line += 1
    codomain = lines[line].split()[1:]
    line += 1
    n = int(lines[line])
    line += 1
    inset = set()
    outset = set()
    for i in range(n):
        a, _, b = lines[line+i].split()
        inset.add(a)
        outset.add(b)
    surjective = len(outset) == len(codomain)
    injective = len(outset) == len(inset)
    if len(inset) != n:
        print('not a function')
    elif injective and surjective:
        print('bijective')
    elif injective:
        print('injective')
    elif surjective:
        print('surjective')
    else:
        print('neither injective nor surjective')
    line += n
