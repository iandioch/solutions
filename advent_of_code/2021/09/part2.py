import sys
from collections import deque

def is_low_point(grid, y, x):
    val = grid[y][x]
    if y > 0 and grid[y-1][x] <= val:
        return False
    if x > 0 and grid[y][x-1] <= val:
        return False
    if y < len(grid)-1 and grid[y+1][x] <= val:
        return False
    if x < len(grid[0]) - 1 and grid[y][x+1] <= val:
        return False

    return True

def flood_fill(grid, colour, start_y, start_x, output):
    seen = set()
    q = deque([(start_y, start_x)])
    size = 0
    while len(q):
        y, x = q.popleft()
        if (y,x) in seen:
            continue
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]):
            continue
        if grid[y][x] == 9:
            continue
        seen.add((y, x))
        size += 1

        output[y][x] = colour

        q.append((y+1, x))
        q.append((y-1, x))
        q.append((y, x+1))
        q.append((y, x-1))

    return size

def main():
    grid = [list(map(int, line.strip())) for line in sys.stdin.readlines()]

    tot = 0

    lows = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if is_low_point(grid, y, x):
                lows.append((y, x))
                tot += (1 + grid[y][x])

    colours = [[-1 for _ in row] for row in grid]
    basin_size = [0 for _ in lows]
    for i in range(len(lows)):
        basin_size[i] = flood_fill(grid, i, lows[i][0], lows[i][1], colours)


    import heapq
    basins = list(range(len(lows)))
    largest = heapq.nlargest(3, basins, key = lambda x: basin_size[x])
    largest_size = [basin_size[x] for x in largest]
    print(largest_size[0] * largest_size[1] * largest_size[2])

main()
