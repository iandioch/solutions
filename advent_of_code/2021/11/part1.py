import sys

NEIGHBOURS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

def main():
    grid = [list(map(int, line.strip())) for line in sys.stdin.readlines()]
    tot = 0
    for step in range(100):
        for row in grid:
            for i in range(len(row)):
                row[i] += 1

        flashed = set()
        done = False
        while not done:
            done = True
            for j in range(len(grid)):
                for i in range(len(grid[i])):
                    if grid[j][i] > 9:
                        flashed.add((j, i))
                        grid[j][i] = -10000000
                        done = False
                        for neighbour in NEIGHBOURS:
                            p = i + neighbour[0]
                            q = j + neighbour[1]
                            if (q >= 0 and q < len(grid) and p >= 0 and p < len(grid[0])):
                                grid[q][p] += 1

        tot += len(flashed)
        for j, i in flashed:
            grid[j][i] = 0
        print(f'{len(flashed)} flashed on step {step+1}.')

    print(tot)

main()



