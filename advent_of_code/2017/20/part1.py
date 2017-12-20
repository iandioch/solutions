import sys

particles = []
best = None
ans = []
for line in sys.stdin.readlines():
    parts = line.split(' ')
    pos = tuple(map(int,parts[0][3:-2].split(',')))
    vel = tuple(map(int,parts[1][3:-2].split(',')))
    acc = tuple(map(int,parts[2][3:-2].split(',')))
    particles.append((pos, vel, acc))

    tot = sum(map(abs, acc))
    if best is None or tot < best:
        best = tot
        ans = [len(particles)-1]
    elif tot == best:
        ans.append(len(particles)-1)

print(min(ans, key = lambda a:sum(map(abs, particles[a][1]))))
