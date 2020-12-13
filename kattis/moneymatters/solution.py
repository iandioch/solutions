V, E = map(int, input().split())
parent = [i for i in range(V)]
balance = [int(input()) for _ in range(V)]

def union(a, b):
    parent[find(a)] = find(b)

def find(a):
    while True:
        a = parent[a]
        if a == parent[a]:
            return a

for _ in range(E):
    a, b = map(int, input().split())
    union(a, b)

def is_poss():
    from collections import defaultdict
    group = [find(v) for v in range(V)]
    group_balance = defaultdict(int)
    done = set()
    for v in range(V):
        group_balance[group[v]] += balance[v]
    return all(group_balance[g] == 0 for g in group_balance)

print(['IMPOSSIBLE', 'POSSIBLE'][int(is_poss())])
