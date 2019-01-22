# Kruskal's algorithm for minimum spanning tree.
parent = {}
rank = {}

def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(vertex_a, vertex_b):
    root_a = find(vertex_a)
    root_b = find(vertex_b)
    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
    if rank[root_a] == rank[root_b]:
        rank[root_b] += 1

def kruskal(graph):
    mst = set()
    edges = list(graph['edges'])
    edges.sort()
    for vertex in graph['vertices']:
        make_set(vertex)
    for edge in edges:
        weight, vertex_a, vertex_b = edge
        if find(vertex_a) != find(vertex_b):
            union(vertex_a, vertex_b)
            mst.add(edge)
    return sorted(mst)

def main():
    while True:
        Nodes, Edges = map(int, input().split())
        if Nodes == Edges == 0:
            return
        e = []
        vert = [i for i in range(Nodes)]
        for _ in range(Edges):
            u, v, weight = map(int, input().split())
            u, v = sorted((u, v))
            e.append((weight, u, v))
        g = {'edges': e, 'vertices': vert}
        mst = kruskal(g)
        tot = sum(a[0] for a in mst)
        ans = sorted((a[1], a[2]) for a in mst)
        if len(ans) == Nodes - 1:
            print(tot)
            for e in ans:
                print(*e)
        else:
            print('Impossible')


    
if __name__ == '__main__':
    main()
