import collections

w, h = [int(x) for x in raw_input().split()]
grid = []
px, py = 0, 0
for y in xrange(h):
	grid.append(raw_input())
	if 'P' in grid[-1]:
		px = grid[-1].index('P')
		py = y

q = collections.deque()
q.append((px, py))

a = 0

TRAP = 'T'
GOLD = 'G'
WALL = '#'

visited = set()

while len(q):
	x, y = q.popleft()
	if (x, y) in visited:
		continue
	visited.add((x, y))
	if grid[y][x] == GOLD:
		a += 1
	if grid[y][x] == WALL:
		continue
	if grid[y-1][x] != TRAP and grid[y+1][x] != TRAP and grid[y][x-1] != TRAP and grid[y][x+1] != TRAP:
		q.append((x, y-1))
		q.append((x, y+1))
		q.append((x-1, y))
		q.append((x+1, y))

print a
