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

    def all_connected():
        groups = []
        for g in group:
            p = find(g)
            if not len(groups):
                groups.append(p)
            elif groups[0] == p:
                continue
            else:
                return False
        return True


    d = list(sorted(dists, key=lambda x:dists[x]))

    for i in range(100000):
        a, b = d[i]
        union(a, b)
        if all_connected():
            print('All connected:', i)
            print(points[a], points[b])
            print(points[a][0] * points[b][0])
            return

main()
