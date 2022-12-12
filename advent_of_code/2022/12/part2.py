import sys
import collections

def get_input():
    grid = []
    start = (0, 0)
    for j, line in enumerate(sys.stdin.readlines()):
        if not len(line.strip()):
            continue
        grid.append([])
        for i, c in enumerate(line.strip()):
            val = -1
            if c == 'S':
                #start = (j, i)
                val = ord('a')
            elif c == 'E':
                start = (j, i)
                val = ord('z')
            else:
                val = ord(c)
            grid[j].append(val)

    return grid, start

def shortest_path(grid, start):

    def can_walk(j, i, b, a):
        if b < 0 or a < 0 or b >= len(grid) or a >= len(grid[0]):
            return False
        # reversed criterion since part 1
        return grid[j][i] <= grid[b][a] + 1

    q = collections.deque()
    q.append((start, 0))
    best = {}
    while len(q):
        pos, steps = q.popleft()
        if pos in best and best[pos] <= steps:
            continue
        print(pos, steps, chr(grid[pos[0]][pos[1]]))
        best[pos] = steps
        (j, i) = pos
        if chr(grid[j][i]) == 'a':
            return steps
        for next_pos in [(j-1, i), (j, i-1), (j+1, i), (j, i+1)]:
            if can_walk(j, i, *next_pos):
                q.append((next_pos, steps + 1))



def main():
    print(shortest_path(*get_input()))

main()
