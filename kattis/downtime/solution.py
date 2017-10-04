from math import ceil

num_req, rps = map(int, input().split())
heap = []
for _ in range(num_req):
    n = int(input())
    heap.append((n, 1))
    heap.append((n+1000, -1))
heap = sorted(heap)
top = 0
curr = 0
for _, d in heap:
    curr += d
    top = max(top, curr)

print(ceil(top/rps))
