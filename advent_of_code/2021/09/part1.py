import sys

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

def main():
    grid = [list(map(int, line.strip())) for line in sys.stdin.readlines()]

    tot = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if is_low_point(grid, y, x):
                tot += (1 + grid[y][x])

    print(tot)

main()
