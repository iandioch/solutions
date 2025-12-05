import sys

def is_removable(grid, x, y):
    if grid[y][x]:
        # Nothing to remove
        return False
    n = 0
    for i in range(x-1, x + 2):
        if i < 0:
            continue
        if i >= len(grid[0]):
            break
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            if j < 0:
                continue
            if j >= len(grid):
                break
            if not grid[j][i]:
                n += 1
    return n < 4

def main():
    grid = []
    for line in sys.stdin.readlines():
        grid.append([c != '@' for c in line.strip()])

    ans = 0
    ok = True
    while ok:
        ok = False
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if is_removable(grid, x, y):
                    ans += 1
                    grid[y][x] = True
                    ok = True

    print(ans)

main()
