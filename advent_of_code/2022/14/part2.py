import sys

DEBUG = False

def parse():
    BUFFER_TOP = 5
    BUFFER_EDGE = 250
    segs = []
    minx, miny, maxx, maxy = 500, 500, 0, 0

    for line in sys.stdin.readlines():
        line = line.strip()
        point = [tuple(map(int, p.split(','))) for p in line.split(' -> ')]
        for i in range(1, len(point)):
            segs.append((point[i-1], point[i]))
            print(segs[-1])

    minx = min(min(s[0][0], s[1][0]) for s in segs)
    maxx = max(max(s[0][0], s[1][0]) for s in segs)
    maxy = max(max(s[0][1], s[1][1]) for s in segs)
    segs.append(((minx-BUFFER_EDGE, maxy+2), (maxx+BUFFER_EDGE, maxy+2)))
    minx -= BUFFER_EDGE
    maxx += BUFFER_EDGE
    maxy += 2

    #miny = min(min(s[0][1], s[1][1]) for s in segs) - BUFFER_TOP
    miny = 0

    grid = [['.' for _ in range(minx, maxx+1)] for _ in range(miny, maxy+1)]
    for start, end in segs:
        if start[0] == end[0]:
            if start[1] > end[1]:
                start, end = end, start
            for y in range(start[1]-miny, end[1]-miny+1):
                grid[y][start[0]-minx] = '#'
        else:
            if start[0] > end[0]:
                start, end = end, start
            for x in range(start[0]-minx, end[0]-minx+1):
                grid[start[1]-miny][x] = '#'
    print('-'*len(grid[0]))
    for row in grid:
        print(''.join(row))

    return grid, 500 - minx

def how_much_sand(grid, sandx):
    def add_sand():
        x = sandx
        y = 0
        if grid[y][x] != '.':
            return False
        while True:
            if y + 1 >= len(grid):
                print('ERROR!')
                return False

            if DEBUG:
                print('-'*len(grid[0]))
                print('in sand:', y, x)
                for j, row in enumerate(grid):
                    print(''.join('+' if (i==x and j==y) else c for i, c in enumerate(row)))
            if grid[y+1][x] == '.':
                y += 1
                continue
            if grid[y+1][x-1] == '.':
                y += 1
                x -= 1
                continue
            if grid[y+1][x+1] == '.':
                y += 1
                x += 1
                continue
            grid[y][x] = 'o'
            return True

    ans = 0
    while True:
        if not add_sand():
            break
        ans += 1
        if DEBUG:
            print('-'*len(grid[0]))
            for row in grid:
                print(''.join(row))
    
    print()
    for row in grid:
        print(''.join(row))
    return ans

def main():
    grid, sandx = parse()
    print(how_much_sand(grid, sandx))

main()
