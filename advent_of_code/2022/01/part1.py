import sys

elves = []
curr = []
for line in sys.stdin.readlines():
    if line.strip() == '':
        elves.append(curr)
        curr = []
    else:
        curr.append(int(line))
elves.append(curr)

print(max(sum(c) for c in elves))
