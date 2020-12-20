import enum
import sys
import operator
from collections import defaultdict, deque
from functools import reduce, lru_cache

NEIGHBOURS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
ORIENTATIONS = [(num_rot, horiz_flip, vertical_flip)
        for num_rot in range(2)
        for horiz_flip in [False, True]
        for vertical_flip in [False, True]]

@lru_cache(maxsize=None)
def get_rotated_tile(grid, num_rotations, horizontal_flip, vertical_flip):
    out = grid[:]
    for i in range(num_rotations):
        out = tuple(zip(*out[::-1])) # fancy shortcut to rotate 90deg
    if horizontal_flip:
        out = [o[::-1] for o in out]
    if vertical_flip:
        out = out[::-1]
    return out

def tiles_match(placed_tile, new_tile, direction):
    if direction == (1, 0):
        # check the placed_tile goes on the right of the new_tile
        return [o[0] for o in placed_tile] == [o[-1] for o in new_tile]
    elif direction == (-1, 0):
        # check the placed_tile goes on the left of the new_tile
        return [o[-1] for o in placed_tile] == [o[0] for o in new_tile]
    elif direction == (0, -1):
        # check the placed_tile goes above the new_tile
        return placed_tile[-1] == new_tile[0]
    else:
        # check the placed_tile goes below the new_tile
        return placed_tile[0] == new_tile[-1]

def get_grid_string(grid, rotation, tiles):
    # Get the compiled grid, without borders, based on the positions in 'grid'.
    # Returns a tuple of strings (one item for each row of the grid).
    ids = get_grid_ids(grid)
    out_grid = [['X' for x in range(8*len(ids[0]))] for y in range(8*len(ids))]
    for y in range(len(ids)):
        for x in range(len(ids[0])):
            tile_id = ids[y][x]
            tile_grid = get_rotated_tile(tiles[tile_id], *rotation[tile_id])
            for j in range(8):
                for i in range(8):
                    out_grid[y*8 + j][x*8 + i] = tile_grid[j+1][i+1]
    return tuple(''.join(o) for o in out_grid)

# A hacky wrapper around assemble_grid. The starting tile's flips (horizontal
# and/or vertical) may make the rest of the grid unsolvable, so try every
# combination until one works...
# Note: I'm not sure if the fact that it makes it unsolvable is because of a bug
# in assemble_grid() or not, but this works, so ¯\_(ツ)_/¯
def outer_assemble_grid(tiles, adjacency):
    for starting_rot in [(False, False), (True, True), (False, True), (True, False)]:
        grid, rotation = assemble_grid(tiles, adjacency, starting_rot)
        if grid is not None:
            return grid, rotation

def assemble_grid(tiles, adjacency, starting_rot):
    rotation = {} # maps tile ID to tuple(num_rotations:int, horiz_flip:bool, vertical_flip:bool)
    grid = {} # maps tuple(x,y) to tile ID
    remaining = set(tiles)

    # Start with a corner, and fill out from there.
    # The starting tile does seem to matter in this impl, which suggests a bug
    # somewhere in it...
    starting_tile = min(t for t in tiles if len(adjacency[t]) == 2)
    grid[(0,0)] = starting_tile
    rotation[starting_tile] = (0, starting_rot[0], starting_rot[1])
    remaining.remove(starting_tile)

    q = deque(NEIGHBOURS)
    while len(q):
        pos = q.popleft()
        if pos in grid:
            # We've already placed a tile here.
            continue
        found = False
        for tile in remaining:
            # Check every as-yet-unplaced tile, and see if it fits in this spot,
            # in any orientation. There should be exactly one, unless this spot
            # is outside of the grid.
            for orientation in ORIENTATIONS:
                tile_grid = get_rotated_tile(tiles[tile], *orientation)

                # Try all of the tiles already placed which border this spot;
                # if any of them matches the tile we're trying to place, go for
                # it!
                # It shouldn't occur that one already-placed tile matches and 
                # another one doesn't, so we just don't check that case...
                matching_neighbours = 0
                for direction in NEIGHBOURS:
                    neighbour_pos = (pos[0] + direction[0],
                                     pos[1] + direction[1])
                    if neighbour_pos not in grid:
                        continue
                    neighbour = grid[neighbour_pos]
                    if not tiles_match(get_rotated_tile(tiles[neighbour],
                                                        *rotation[neighbour]),
                                       tile_grid, direction):
                        break
                    matching_neighbours += 1
                if matching_neighbours >= 1:
                    found = True
                    grid[pos] = tile
                    rotation[tile] = orientation
                    remaining.remove(tile)
                    break
            if found:
                # Stop looking at other tiles...
                break
        if found:
            for n in NEIGHBOURS:
                next_pos = (pos[0] + n[0], pos[1] + n[1])
                q.append(next_pos)

    print('Tiles remaining after assembling grid, starting at tile {} ' \
          '(with rotation {}): {}'.format(
              starting_tile, starting_rot, len(remaining)))
    if len(remaining):
        # If there are remaining tiles, don't count this as a valid grid
        # arrangement, and return None.
        return None, None
    return grid, rotation

def get_grid_ids(grid):
    minx = min(x[0] for x in grid)
    maxx = max(x[0] for x in grid)
    miny = min(x[1] for x in grid)
    maxy = max(x[1] for x in grid)

    out = []
    for y in range(miny, maxy+1):
        row = []
        for x in range(minx, maxx+1):
            pos = (x,y)
            if pos in grid:
                row.append(grid[pos])
            else:
                row.append(None)
        out.append(row)
    return out

# debug_rot here is just a string identifier to optionally print.
def count_monsters(grid_str, debug_rot=None):
    MONSTER = ['                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ']
    MON_WIDTH = len(MONSTER[0])
    MON_HEIGHT = 3
    num_monster = 0
    for y in range(len(grid_str) - MON_HEIGHT + 1):
        for x in range(len(grid_str[y]) - MON_WIDTH + 1):
            matches_monster = True
            for j in range(MON_HEIGHT):
                for i in range(MON_WIDTH):
                    if MONSTER[j][i] == ' ':
                        continue
                    if grid_str[y+j][x+i] != '#':
                        matches_monster = False
                        break
            if matches_monster:
                num_monster += 1
    tot = 0
    for y in range(len(grid_str)):
        for x in range(len(grid_str[0])):
            if grid_str[y][x] == '#':
                tot += 1
    ans = tot - num_monster*15
    if debug_rot is not None:
        print('For rotation {}:\t'.format(debug_rot), end=' ')
    print('{:03d}/{:04d} #s are part of a monster.\tAns: {}'.format(
        num_monster*15, tot, ans))
    return ans

def main():
    tiles = {} 
    pattern_to_tile = defaultdict(list)
    tile_to_pattern = defaultdict(list)
    def add_tile(name, lines):
        name_num = int(name.split()[1][:-1])
        tiles[name_num] = tuple(lines)
        # top and bottom both ways
        patterns = [lines[0], lines[-1], lines[0][::-1], lines[-1][::-1]]
        # two sides
        patterns.append(''.join(lines[i][0] for i in range(10)))
        patterns.append(patterns[-1][::-1])
        patterns.append(''.join(lines[i][-1] for i in range(10)))
        patterns.append(patterns[-1][::-1])
        for pattern in patterns:
            pattern_to_tile[pattern].append(name_num)
            tile_to_pattern[name_num].append(pattern)

    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        name = lines[i].strip()
        grid = [line.strip() for line in lines[i+1:i+11]]
        add_tile(name, grid)
        i += 12

    adjacency = defaultdict(set)
    for pattern in pattern_to_tile:
        tile = pattern_to_tile[pattern]
        if len(tile) >= 2:
            for t in tile:
                adjacency[t].update(s for s in tile if s != t)

    # No pattern should be shared by > 2 tiles...
    for pattern in pattern_to_tile:
        if len(pattern_to_tile[pattern]) > 2:
            print('Uh oh, pattern {} has more than 2 tiles: {}'.format(
                pattern, pattern_to_tile[pattern]))

    grid, rotation = outer_assemble_grid(tiles, adjacency)

    # Print the IDs of each tile for debugging.
    grid_ids = get_grid_ids(grid)
    for row in grid_ids:
        print(row)
    
    # Print debug grid including borders, with gaps between tiles.
    out_grid = [[' ' for x in range(11*len(grid_ids[0]))]
                     for y in range(11*len(grid_ids))]
    for y in range(len(grid_ids)):
        for x in range(len(grid_ids[0])):
            tile_id = grid_ids[y][x]
            tile_grid = get_rotated_tile(tiles[tile_id], *rotation[tile_id])
            for j in range(10):
                for i in range(10):
                    out_grid[y*11 + j][x*11 + i] = tile_grid[j][i]
    print('\n'.join(''.join(row) for row in out_grid))

    # Print the real grid without borders.
    grid_str = get_grid_string(grid, rotation, tiles)
    print('\n'.join(row for row in grid_str))

    # Try each rotation and find the one which the number of non-monster #s is
    # minimised.
    minn = 100000000
    for o in ORIENTATIONS:
        rot_grid = get_rotated_tile(grid_str, *o)
        monst = count_monsters(rot_grid, debug_rot=o)
        minn = min(minn, monst)
    print('Answer:', minn)
    #print(get_grid_ids(assemble_grid(tiles, adjacency)))


main()
