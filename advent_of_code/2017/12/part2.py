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

num_set = 0
remaining = set(d.keys())
while len(remaining):
    num_set += 1
    start = remaining.pop()
    connected = set()
    tbd = set([start])
    while len(tbd):
        s = tbd.pop()
        connected.add(s)
        for t in d[s].connect:
            if t in connected:
                continue
            tbd.add(t)
    remaining -= connected

print(num_set)
