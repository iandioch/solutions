ntests = int(input())

parent = None
# a dict {x:str}, where str is x's parent
# however, if x has no parent, str is an int of the number of
# descendants x has

def find(x):
    p = x
    while type(parent[p]) is not int:
        p = parent[p]

    while parent[x] != p:
        # compress the path
        x, parent[x] = parent[x], p

    return p

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return parent[x]
    if parent[x] < parent[y]:
        x, y = y, x
    parent[x] += parent[y]
    parent[y] = x
    return parent[x]
        
    
for test in range(ntests):
    n = int(input())
    parent = {}

    for i in range(n):
        a, b = input().split()
        if a not in parent:
            parent[a] = 1
        if b not in parent:
            parent[b] = 1
        a = union(a, b)
        print(a)
