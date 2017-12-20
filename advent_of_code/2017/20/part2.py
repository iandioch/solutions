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

for tick in range(50):
    np = []
    for part in particles:
        pos = list(part[0])
        vel = list(part[1])
        acc = part[2]

        for i in range(3):
            vel[i] += acc[i]
        for i in range(3):
            pos[i] += vel[i]
        np.append((tuple(pos), tuple(vel), acc))

    bye = set()
    for i in range(len(np)):
        for j in range(i+1, len(np)):
            if np[i][0] == np[j][0]:
                bye.add(j)
                bye.add(i)

    for i in sorted(bye, reverse=True):
        del np[i]
    particles = np

print(len(particles))
