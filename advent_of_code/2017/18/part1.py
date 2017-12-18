import sys
from collections import defaultdict

reg = defaultdict(int)
played = []

def get_val(s):
    if s[0] == '-':
        return int(s)
    if s.isdigit():
        return int(s)
    return reg[s]

def exec(p):
    if p[0] == 'snd':
        played.append(get_val(p[1]))
    elif p[0] == 'set':
        reg[p[1]] = get_val(p[2])
    elif p[0] == 'add':
        reg[p[1]] += get_val(p[2])
    elif p[0] == 'mul':
        reg[p[1]] *= get_val(p[2])
    elif p[0] == 'mod':
        reg[p[1]] %= get_val(p[2])
    elif p[0] == 'rcv':
        if get_val(p[1]) != 0:
            print(played[-1])
            return 10**10
    elif p[0] == 'jgz':
        if get_val(p[1]) > 0:
            return get_val(p[2])
    return 1

lines = [s.split() for s in sys.stdin.readlines()]

curr = 0
while True:
    jump = exec(lines[curr])
    curr += jump
    if curr >= len(lines) or curr < 0:
        break
