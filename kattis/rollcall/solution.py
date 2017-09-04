import sys

names = [line.split() for line in sys.stdin.readlines()]

seen = set()
repeat = set()

for first, last in names:
    if first in seen:
        repeat.add(first)
    seen.add(first)

names.sort(key=lambda x: x[0])
names.sort(key=lambda x: x[1])
for first, last in names:
    if first in repeat:
        print(first, last)
    else:
        print(first)
