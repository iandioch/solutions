import heapq
from collections import deque

h, w = map(int, raw_input().split())
grid = [raw_input() for _ in xrange(h)]

dist = [[1000000 for _ in xrange(w)] for _ in xrange(h)]

q = deque()
start = None
goal = None
for y in xrange(h):
    for x in xrange(w):
        if grid[y][x] == '+':
            q.append((-1, y, x))
        elif grid[y][x] == 'V':
            start = (y,x)
        elif grid[y][x] == 'J':
            goal = (y,x)

while len(q):
    d, y, x = q.popleft() 
    d += 1
    if dist[y][x] <= d:
        continue
    dist[y][x] = d
    if y > 0 and dist[y-1][x] > d+1:
        q.append((d, y-1, x))
    if x > 0 and dist[y][x-1] > d+1:
        q.append((d,y,x-1))
    if y < h-1 and dist[y+1][x] > d+1:
        q.append((d,y+1,x))
    if x < w-1 and dist[y][x+1] > d+1:
        q.append((d,y,x+1))

q = [(-dist[start[0]][start[1]], start[0], start[1])]

visited = [[False for _ in range(w)] for _ in range(h)]

while len(q):
    d, y, x = heapq.heappop(q)
    if visited[y][x]:
        continue
    visited[y][x] = True
    d = max(d, -dist[y][x])
    if goal[0] == y and goal[1] == x:
        print(-d)
        break
    if y > 0 and not visited[y-1][x]:
        heapq.heappush(q, (d, y-1, x))
    if x > 0 and not visited[y][x-1]:
        heapq.heappush(q, (d, y, x-1))
    if y < h-1 and not visited[y+1][x]:
        heapq.heappush(q, (d, y+1, x))
    if x < w-1 and not visited[y][x+1]:
        heapq.heappush(q, (d, y, x+1))
