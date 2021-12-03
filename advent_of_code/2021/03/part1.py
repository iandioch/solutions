import sys
from collections import defaultdict

lines = [s.strip() for s in sys.stdin.readlines()]
count = [defaultdict(int) for _ in range(len(lines[0]))]
for line in lines:
    for i in range(len(line)):
        count[i][line[i]] += 1

gamma = []
epsilon = []
for i in range(len(line)):
    gamma.append(max(count[i], key = lambda x: count[i][x]))
    epsilon.append(min(count[i], key = lambda x: count[i][x]))
gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)
print('gamma:', gamma)
print('epsilon:', epsilon)
print(gamma * epsilon)

