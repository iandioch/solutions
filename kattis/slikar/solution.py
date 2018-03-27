import heapq

h, w = map(int, input().split())
rows = [input().strip() for _ in range(h)]

flood_time = [[9999999 for x in row] for row in rows]
walk_time = [[9999999 for x in row] for row in rows]
 
q = []
for j in range(h):
    for i in range(w):
        if rows[j][i] == '*':
            heapq.heappush(q, (0, i, j))

while q:
    curr, x, y = heapq.heappop(q)
    if y < 0 or x < 0 or y >= h or x >= w:
        continue 
    if flood_time[y][x] <= curr:
        continue
    if rows[y][x] == 'D' or rows[y][x] == 'X':
        continue 
    flood_time[y][x] = curr
    heapq.heappush(q, (curr+1, x+1, y))
    heapq.heappush(q, (curr+1, x-1, y))
    heapq.heappush(q, (curr+1, x, y-1))
    heapq.heappush(q, (curr+1, x, y+1))

q = []
target = None
for j in range(h):
    for i in range(w):
        if rows[j][i] == 'S':
            heapq.heappush(q, (0, i, j))
        elif rows[j][i] == 'D':
            target = (i, j)

while q:
    curr, x, y = heapq.heappop(q)
    if y < 0 or x < 0 or y >= h or x >= w:
        continue 
    if flood_time[y][x] <= curr:
        continue
    if rows[y][x] == 'X':
        continue 
    if walk_time[y][x] <= curr:
        continue
    walk_time[y][x] = curr
    if rows[y][x] == 'D':
        continue
    heapq.heappush(q, (curr+1, x+1, y))
    heapq.heappush(q, (curr+1, x-1, y))
    heapq.heappush(q, (curr+1, x, y-1))
    heapq.heappush(q, (curr+1, x, y+1))

ans = walk_time[target[1]][target[0]]
if ans >= 9999999:
    print('KAKTUS')
else:
    print(ans)
