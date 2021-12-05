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
        a, b = start
        p, q = end
        minx = min(a, p)
        miny = min(b, q)
        maxx = max(a, p)
        maxy = max(b, q)

        if a == p:
            for y in range(miny, maxy + 1):
                grid[y][start[0]] += 1
        if b == q:
            for x in range(minx, maxx + 1):
                grid[start[1]][x] += 1
        if (abs(a-b) == abs(p-q)) or (abs(a-p) == abs(b-q)):
            i, j = a, b
            while i != p:
                grid[j][i] += 1
                if i < p:
                    i += 1
                else:
                    i -= 1
                if j < q:
                    j += 1
                else:
                    j -= 1
            grid[j][i] += 1

    PRINT = False
    tot = 0
    for col in grid:
        for p in col:
            if PRINT:
                print('.' if p == 0 else p, end=' ')
            if p >= 2:
                tot += 1
        if PRINT:
            print()

    print(tot)

main()

