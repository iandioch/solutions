import sys
from collections import defaultdict

reg = [defaultdict(int), defaultdict(int)]
reg[1]['p'] = 1
queue = [[], []]

sent = [0,0]

def get_val(s, pid):
    if s[0] == '-':
        return int(s)
    if s.isdigit():
        return int(s)
    return reg[pid][s]

def exec(p, pid):
    other = (pid+1)%2
    if p[0] == 'snd':
        queue[other].append(get_val(p[1], pid))
        sent[pid] += 1
    elif p[0] == 'set':
        reg[pid][p[1]] = get_val(p[2], pid)
    elif p[0] == 'add':
        reg[pid][p[1]] += get_val(p[2], pid)
    elif p[0] == 'mul':
        reg[pid][p[1]] *= get_val(p[2], pid)
    elif p[0] == 'mod':
        reg[pid][p[1]] %= get_val(p[2], pid)
    elif p[0] == 'rcv':
        if len(queue[pid]) > 0:
            reg[pid][p[1]] = queue[pid].pop(0)
        else:
            return 0
    elif p[0] == 'jgz':
        if get_val(p[1], pid) > 0:
            return get_val(p[2], pid)
    return 1

lines = [s.split() for s in sys.stdin.readlines()]

a, b = 0, 0
while True:
    aj = exec(lines[a], 0)
    bj = exec(lines[b], 1)
    if aj == 0 and bj == 0:
        print('deadlock')
        break
    a += aj
    b += bj

print(sent[1])
