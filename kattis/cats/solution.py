import heapq

def prims(N, edges):
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
            dist = edges[u][v]
            if dist > tree_dist[v]:
                continue
            tree_dist[v] = dist
            heapq.heappush(pq, (dist, v))
    return cost

def main():
    T = int(input())
    for _ in range(T):
        Milk, Cats = map(int, input().split())
        e = [[0]*Cats for _ in range(Cats)]
        for _ in range((Cats*(Cats-1))//2):
            i, j, d = map(int, input().split())
            e[i][j] = d
            e[j][i] = d
        ans = prims(Cats, e)
        if ans + Cats <= Milk:
            print('yes')
        else:
            print('no')
    
if __name__ == '__main__':
    main()
