import sys

dirs = {
    'D': (1, 0),
    'U': (-1, 0),
    'R': (0, 1),
    'L': (0, -1),
}

lines = sys.stdin.readlines()
y = 0
x = 0
for xi in range(len(lines[0])):
    if lines[0][xi] == '|':
        x = xi
        break

path = []
d = 'D'
curr = (y, x)

while True:
    if lines[curr[0]][curr[1]] == ' ':
        break
    if lines[curr[0]][curr[1]] == '+':
        for e in dirs:
            diff = dirs[e]
            currdiff = dirs[d]
            if diff[0] + currdiff[0] == 0 and diff[1] + currdiff[1] == 0:
                continue
            f = tuple(map(sum, zip(curr, diff)))
            if lines[f[0]][f[1]] != ' ':
                d = e
                break
    if lines[curr[0]][curr[1]] not in set('-+|'):
        path.append(lines[curr[0]][curr[1]])
    diff = dirs[d]
    curr = tuple(map(sum, zip(curr, diff)))


print(''.join(path))
