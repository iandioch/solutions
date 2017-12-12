import sys
from collections import defaultdict

class Node:
    def __init__(self):
        self.connect = []

d = defaultdict(Node)

for line in sys.stdin.readlines():
    p = line.split()
    base = p[0]
    for other in p[2:]:
        other = other.strip(',')
        d[base].connect.append(other)

zero_set = set()
tbd = set(['0'])
while len(tbd):
    s = tbd.pop()
    zero_set.add(s)
    for t in d[s].connect:
        if t in zero_set:
            continue
        tbd.add(t)

print(len(zero_set))
