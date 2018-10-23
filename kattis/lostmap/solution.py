import heapq

def prims(N, dists):
    cost = 0
    pq = [(0, 0, 0)]
    in_tree = [False] * N
    tree_dist = [1000000] * N
    tree_size = 0

    mst = []
    while tree_size < N and pq:
        d, u, prev = heapq.heappop(pq)
        if in_tree[u]:
            continue
        mst.append((prev, u))
        in_tree[u] = True
        cost += d
        tree_size += 1
        for v in range(N):
            if u == v or in_tree[v]:
                continue
            dist = dists[u][v]
            if dist > tree_dist[v]:
                continue
            tree_dist[v] = dist
            heapq.heappush(pq, (dist, v, u))
    return mst[1:]

def main():
    n = int(input())
    e = [list(map(int, input().split())) for _ in range(n)]
    mst = prims(n, e)
    for r in mst:
        a, b = r
        print(a+1, b+1)

if __name__ == '__main__':
    main()
