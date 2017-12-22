import sys

class Mapping:
    def __init__(self, s, o):
        self.s = s
        self.grid = [list(t) for t in s.split('/')]
        self.output = [list(t) for t in o.split('/')]

    @staticmethod
    def grids_match(a, b):
        c = a[:]
        for rotate in range(4):
            flipped = [t[::-1] for t in c]
            if flipped == b:
                return True
            rotated = [list(t) for t in zip(*c[::-1])]
            if rotated == b:
                return True
            c = rotated
        return False

    def matches(self, other_grid):
        if len(self.grid) != len(other_grid):
            return False
        return Mapping.grids_match(self.grid, other_grid)


mappings = []

for line in sys.stdin.readlines():
    p = line.strip().split(' => ')
    mappings.append(Mapping(p[0], p[1]))

pattern = [list(s) for s in '.#./..#/###'.split('/')]
for step in range(5):
    old_size = None
    if len(pattern) % 2 == 0:
        # break the pixels up into 2x2 squares, and convert each 2x2 square into a 3x3 square 
        old_size = 2
    else:
        # break the pixels up into 3x3 squares, and convert each 3x3 square into a 4x4 square
        old_size = 3
    new_size = old_size + 1
    num = len(pattern) // old_size
    new_array = [[None for _ in range(new_size*num)] for _ in range(new_size*num)]
    for y in range(num):
        for x in range(num):
            subarray = []
            for j in range(old_size):
                subarray.append(pattern[y*old_size + j][x*old_size:(x+1)*old_size])
            for mapping in mappings:
                if mapping.matches(subarray):
                    for j in range(new_size):
                        for k in range(new_size):
                            new_array[y*new_size + j][x*new_size + k] = mapping.output[j][k]
                    break
    pattern = new_array


ans = sum(s.count('#') for s in pattern)
print(ans)
