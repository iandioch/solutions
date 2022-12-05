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

tot = list(sorted((sum(e) for e in elves), reverse=True))
print(sum(tot[:3]))
