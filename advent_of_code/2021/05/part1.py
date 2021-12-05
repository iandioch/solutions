import sys

def main():
    vents = []


    minx = 1000000
    miny = minx
    maxx = 0
    maxy = 0
    for line in sys.stdin.readlines():
        parts = line.split(' -> ')
        a, b = map(int, parts[0].split(','))
        p, q = map(int, parts[1].split(','))

        vents.append(((a, b), (p, q)))
        minx = min(minx, a, p)
        miny = min(miny, b, q)
        maxx = max(maxx, a, p)
        maxy = max(maxy, b, q)

    grid = [[0 for _ in range(maxx+1)] for _ in range(maxy+1)]
    for (start, end) in vents:
        if start[0] == end[0]:
            for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
                grid[y][start[0]] += 1
        if start[1] == end[1]:
            for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
                grid[start[1]][x] += 1

    tot = 0
    for col in grid:
        for p in col:
            if p >= 2:
                tot += 1

    print(tot)

main()

