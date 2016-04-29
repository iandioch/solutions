import sys

grid = [[int(x) for x in line.split()] for line in sys.stdin.readlines()]

max_in_col = [max(g) for g in grid]

sum_of_maxes_from_col = [sum(max_in_col[i:]) for i in xrange(0, len(max_in_col))]


max_so_far = 0

def step(curr_col, sum_so_far, used_so_far):
    global max_so_far
    if curr_col >= len(grid):
        max_so_far = max(max_so_far, sum_so_far)
        return


    if sum_so_far + sum_of_maxes_from_col[curr_col] < max_so_far:
        return sys.maxint

    for i in xrange(0, len(grid[0])):
        if used_so_far[i]:
            continue
        u = used_so_far[:]
        u[i] = True
        step(curr_col+1, sum_so_far + grid[curr_col][i], u)

step(0, 0, [False for i in grid[0]])

print max_so_far
