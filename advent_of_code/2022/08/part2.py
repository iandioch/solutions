import sys

def calc_scenic_score(grid, y, x):
    up = 0
    for j in range(y-1, -1, -1):
        up += 1
        if grid[y][x] <= grid[j][x]:
            break

    down = 0
    for j in range(y+1, len(grid)):
        down += 1
        if grid[y][x] <= grid[j][x]:
            break

    left = 0
    for i in range(x-1, -1, -1):
        left += 1
        if grid[y][x] <= grid[y][i]:
            break

    right = 0
    for i in range(x+1, len(grid[0])):
        right += 1
        if grid[y][x] <= grid[y][i]:
            break

    return up*down*left*right

def main():
    grid = []
    for line in sys.stdin.readlines():
        grid.append([int(c) for c in line.strip()])

    print(max(calc_scenic_score(grid, y, x) for y in range(len(grid)) for x in range(len(grid[0]))))

main()
