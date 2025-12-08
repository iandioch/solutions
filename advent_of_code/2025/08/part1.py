import sys

def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

def main():
    points = []
    for line in sys.stdin.readlines():
        x, y, z = map(int, line.strip().split(','))
        points.append((x, y, z))

    dists = {}
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dists[(i,j)] = dist(points[i], points[j])

    group = {i:i for i in range(len(points))}

    def find(a):
        if group[a] == a:
            return a
        return find(group[a])

    def union(a, b):
        group[find(a)] = find(b)

    d = list(sorted(dists, key=lambda x:dists[x]))

    for i in range(1000):
        a, b = d[i]
        union(a, b)

    groups = {}

    for g in group:
        p = find(g)
        if p in groups:
            groups[p].append(g)
        else:
            groups[p] = [g]

    sg = sorted(groups, key=lambda x: -len(groups[x]))
    n = 1
    for i in range(3):
        n *= len(groups[sg[i]])
    print(n)


main()
