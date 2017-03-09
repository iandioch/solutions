import heapq

num_vert = int(input())

items = [0] + [int(v) for v in input().split()]

connected = [{} for i in range(num_vert+1)]
num_edges = int(input())
for e in range(num_edges):
    a, b, d = map(int, input().split())
    connected[a][b] = d
    connected[b][a] = d

# get from loc 1 to n
# d is a priority queue of tuples (dist, -num_items, curr)
d = []
heapq.heappush(d, (0, 0, 1))
found = False
shortest = [999999999 for i in range(num_vert+1)]

while len(d) > 0:
    dist, n_items, curr = heapq.heappop(d)
    if dist >= shortest[curr]:
        continue
    shortest[curr] = dist
    n_items -= items[curr]


    if curr == num_vert:
        print(dist, -n_items)
        found = True
        break
    for v in connected[curr]:
        if dist+connected[curr][v] <= shortest[v]:
            heapq.heappush(d, (dist+connected[curr][v], n_items, v))

if not found:
    print('impossible')
