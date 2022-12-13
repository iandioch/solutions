import sys

def count_invisible(grid):
    left = [[0 for col in row] for row in grid]
    right = [[0 for col in row] for row in grid]
    up = [[0 for col in row] for row in grid]
    down = [[0 for col in row] for row in grid]

    for y in range(len(grid)):
        for x in range(1, len(grid[y])):
            left[y][x] = max(left[y][x-1], grid[y][x-1])

    for y in range(1, len(grid)):
        for x in range(len(grid[y])):
            up[y][x] = max(up[y-1][x], grid[y-1][x])

    for y in range(len(grid)):
        for x in range(len(grid[y])-2, -1, -1):
            right[y][x] = max(right[y][x+1], grid[y][x+1])

    for y in range(len(grid)-2, -1, -1):
        for x in range(len(grid[y])):
            down[y][x] = max(down[y+1][x], grid[y+1][x])

    ans = 0
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[y])-1):
            if (grid[y][x] <= left[y][x] and
                grid[y][x] <= right[y][x] and
                grid[y][x] <= up[y][x] and
                grid[y][x] <= down[y][x]):
                #invisible
                print(y, x)
                ans += 1
    return len(grid)*len(grid[0]) - ans


def main():
    grid = []
    for line in sys.stdin.readlines():
        grid.append([int(c) for c in line.strip()])

    print(count_invisible(grid))

main()
