import heapq
from collections import defaultdict
num_film, num_horror, num_sim = map(int, input().split())
connected = defaultdict(set)
for i in map(int, input().split()):
    connected[-1].add(i)
for _ in range(num_sim):
    a, b = map(int, input().split())
    connected[a].add(b)
    connected[b].add(a)

q = []
heapq.heappush(q, (0, -1))

val = {}
maxd = 0
while q:
    d, curr = heapq.heappop(q)
    if curr in val and val[curr] <= d:
        continue
    val[curr] = d
    maxd = max(maxd, d)
    for o in connected[curr]:
        heapq.heappush(q, (d + 1, o))

covered_all = (len(val) == num_film + 1)
for i in range(num_film):
    if i not in val:
        print(i)
        break
    if covered_all and val[i] == maxd:
        print(i)
        break

