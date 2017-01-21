import sys

d = {}

for line in sys.stdin.readlines():
    parts = line.split()
    if parts[0] == 'def':
        d[parts[1]] = int(parts[2])
    elif parts[0] == 'clear':
        d = {}
    else:
        # parts[0] = 'calc'
        exp = ' '.join(parts[1:])
        if parts[1] not in d:
            print exp, 'unknown'
            continue
        a = d[parts[1]]
        i = 2
        valid = True
        while parts[i] != '=':
            if parts[i+1] not in d:
                valid = False
                break
            v = d[parts[i+1]]
            if parts[i] == '-':
                a -= v
            elif parts[i] == '+':
                a += v
            i += 2
        if valid:
            k = None
            for j in d:
                if d[j] == a:
                    k = j
            if k == None:
                valid = False
            else:
                print exp, k
        if not valid:
            print exp, 'unknown'
