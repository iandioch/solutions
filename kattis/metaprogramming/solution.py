import sys

var = {}

for line in sys.stdin.readlines():
    p = line.split()
    if p[0][0] == 'd':
        # define
        var[p[2]] = int(p[1])
    else:
        if p[1] not in var or p[3] not in var:
            print('undefined')
            continue
        a = var[p[1]]
        b = var[p[3]]
        op = p[2]
        if op == '=':
            print('true' if a == b else 'false')
        elif op == '>':
            print('true' if a > b else 'false')
        elif op == '<':
            print('true' if a < b else 'false')
