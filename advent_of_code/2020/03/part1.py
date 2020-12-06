import sys

x = 0
y = 0
ans = 0

grid = [s.strip() for s in sys.stdin.readlines()]
height = len(grid)
width = len(grid[0])
while y < height:
    if grid[y][x % width] == '#':
        ans += 1

    x += 3
    y += 1
print(ans)
