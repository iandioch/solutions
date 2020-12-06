import sys

grid = [s.strip() for s in sys.stdin.readlines()]
height = len(grid)
width = len(grid[0])

def count_trees(xd, yd):
    x = 0
    y = 0
    ans = 0
    while y < height:
        if grid[y][x % width] == '#':
            ans += 1

        x += xd
        y += yd

    return ans

ans = 1
for d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    ans *= count_trees(*d)
print(ans)
