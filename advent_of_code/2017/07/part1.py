import sys

parent = {}

for line in sys.stdin.readlines():
    parts = line.split()
    name = parts[0]
    if name not in parent:
        parent[name] = None
    weight_brackets = parts[1]
    if '->' in line:
        a, b = line.split('->')
        dep = b.split(',')
        for d in dep:
            d = d.strip()
            parent[d] = name
            


for p in parent:
    if parent[p] is None:
        print(p)
