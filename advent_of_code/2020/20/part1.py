import sys
import operator
from collections import defaultdict
from functools import reduce

def main():
    tiles = {} 
    pattern_to_tile = defaultdict(list)
    tile_to_pattern = defaultdict(list)
    def add_tile(name, lines):
        name_num = int(name.split()[1][:-1])
        tiles[name_num] = lines
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

    print(tile_to_pattern)
    print(pattern_to_tile)
    for pattern in pattern_to_tile:
        if len(pattern_to_tile[pattern]) > 2:
            print('Uh oh, duplicated pattern:', pattern)
    print(reduce(operator.mul, (tile for tile in tile_to_pattern if len(adjacency[tile]) == 2)))
    #print(tiles)

main()
