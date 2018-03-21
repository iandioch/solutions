import heapq

def sieve(n=10000):
    is_composite = [False for _ in range(n)]
    primes = []
    for i in range(2, n):
        if is_composite[i]:
            continue
        if i > 1000:
            primes.append(i)
        for j in range(i+i, n, i):
            is_composite[j] = True
    return primes


def build_graph(primes):
    ps = [str(p) for p in primes]
    d = {p:{} for p in ps}
    for i in range(len(primes)-1):
        for j in range(i+1, len(primes)):
            p = ps[i]
            q = ps[j]
            nsame = 0

            dig = 0
            for k in range(4):
                if p[k] == q[k]:
                    nsame += 1
                else:
                    dig = k
            if nsame == 3:
                d[p][q] = dig
                d[q][p] = dig
    return d


graph = build_graph(sieve())

def find_route(start, goal):
    q = []
    heapq.heappush(q, (0, start, goal, -1))
    best = None
    visited = set()
    while len(q):
        cost, a, b, prevdig = heapq.heappop(q)
        if a == b:
            return cost
        visited.add(a)
        for other in graph[a]:
            if other in visited:
                continue
            dig = graph[a][other]
            if dig == prevdig:
                continue
            heapq.heappush(q, (cost+1, other, b, dig))
    return None

n = int(input())
for _ in range(n):
    a, b = input().split()
    print(find_route(a, b))
