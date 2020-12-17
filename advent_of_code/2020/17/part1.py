import sys
from collections import defaultdict

DEBUG=False

def get_neighbour_coords(tup):
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == j == k == 0:
                    continue
                yield (tup[0] + i, tup[1] + j, tup[2] + k)

def step(grid):
    out = defaultdict(bool)

    all_neighbours = set()

    def process_pos(pos):
        tot = 0
        for neighbour in get_neighbour_coords(pos):
            all_neighbours.add(neighbour)
            if neighbour in grid and grid[neighbour]:
                tot += 1
        active = (pos in grid and grid[pos])
        if DEBUG:
            print('processing pos ({}): {} with {} neighbours'.format(
                pos, 'active' if active else 'inactive', tot))
        new_active = active
        if active and (tot < 2 or tot > 3):
            new_active = False
        elif tot == 3:
            new_active = True

        # We can just not have things in the grid if they're inactive...
        # That should make the grid smaller and the process faster.
        if new_active:
            out[pos] = new_active

    for pos in grid:
        process_pos(pos)

    # Maybe add some neighbours into the grid
    for pos in all_neighbours - set(out) - set(grid):
        process_pos(pos)

    return out

def print_grid(grid):
    MAX = 15

    minn = [0, 0, 0]
    maxx = [0, 0, 0]
    for z in range(-MAX, MAX):
        for y in range(-MAX, MAX):
            for x in range(-MAX, MAX):
                if (x,y,z) in grid:
                    minn = [min(minn[0], x), min(minn[1], y), min(minn[2], z)]
                    maxx = [max(maxx[0], x), max(maxx[1], y), max(maxx[2], z)]
    for z in range(minn[2], maxx[2] + 1):
        print('z = {}'.format(z))
        for y in range(minn[1], maxx[1] + 1):
            s = ''
            for x in range(minn[0], maxx[0] + 1):
                active = ((x,y,z) in grid) and grid[(x,y,z)]
                s += '#' if active else '.'
            print(s)
        print()


def main():
    grid = defaultdict(bool)

    for y, line in enumerate(sys.stdin.readlines()):
        for x, c in enumerate(line):
            grid[(x, y, 0)] = c == '#'

    for i in range(6):
        print('-'*10)
        print('Grid at i =', i)
        print_grid(grid)
        #for g in grid:
            #print(g, grid[g])
        #print('-'*10)

        grid = step(grid)

    print(sum(1 for g in grid if grid[g]))



main()
