import heapq
from collections import deque

n, start, target = map(int, input().split())

times = []
for _ in range(n):
    times.append(list(map(int, input().split())))

best = [1000000 for _ in range(n)]
q = []
heapq.heappush(q, (0, start))
while len(q):
    time, curr = heapq.heappop(q) 
    if time >= best[curr]:
        continue
    best[curr] = time
    if curr == target:
        break
    for other in range(n):
        if other == curr:
            continue
        t = time + times[curr][other]
        if best[other] <= t:
            continue
        heapq.heappush(q, (t, other))
print(best[target])

