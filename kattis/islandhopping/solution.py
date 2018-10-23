import cmath
import heapq

def complex_dist(a, b):
    return cmath.polar(a - b)[0]

def prims(N, points):
    cost = 0
    pq = [(0, 0)]
    in_tree = [False] * N
    tree_dist = [1000000] * N
    tree_size = 0
    while tree_size < N and pq:
        d, u = heapq.heappop(pq)
        if in_tree[u]:
            continue
        in_tree[u] = True
        cost += d
        tree_size += 1
        for v in range(N):
            if u == v or in_tree[v]:
                continue
            dist = complex_dist(points[u], points[v])
            if dist > tree_dist[v]:
                continue
            tree_dist[v] = dist
            heapq.heappush(pq, (dist, v))
    return cost

def main():
    T = int(input())
    for _ in range(T):
        nislands = int(input())
        pts = []
        for i in range(nislands):
            x, y = map(float, input().split())
            pts.append(complex(x, y))
        mst = prims(nislands, pts)
        print(mst)
    
if __name__ == '__main__':
    main()
