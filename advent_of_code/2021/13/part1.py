import sys

def render(grid):
    print()
    for row in grid:
        print(''.join('#' if c else '.' for c in row))

def main():
    dots = []
    folds = []
    in_folds = False
    width, height = 0, 0
    for line in sys.stdin.readlines():
        line = line.strip()
        if not len(line):
            in_folds = True
            continue
        if in_folds:
            # omit "fold along "
            line = line[11:]
            dimension, coord = line.split('=')
            folds.append((dimension, int(coord)))
        else:
            x,y = map(int, line.split(','))
            width = max(width, x+1)
            height = max(height, y+1)
            dots.append((x,y))

    grid = [[False for _ in range(width)] for _ in range(height)]
    for x,y in dots:
        grid[y][x] = True

    for dimension, coord in folds[:1]:
        render(grid)
        if dimension == 'y':
            # Folding across horizontal line
            new_grid = [row for row in grid[:coord]]
            for y in range(1, coord + 1):
                for x in range(len(grid[0])):
                    new_grid[-y][x] |= grid[coord + y][x]
            grid = new_grid
        else:
            # Folding across vertical line
            new_grid = [row[:coord] for row in grid]
            for y in range(len(grid)):
                for x in range(1, coord + 1):
                    new_grid[y][-x] |= grid[y][coord + x]
            grid = new_grid
    render(grid)

    ans = 0
    for row in grid:
        for col in row:
            if col:
                ans += 1

    print(ans)


main()
