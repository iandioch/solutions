from itertools import groupby

numtests = int(input())
for test in range(numtests):
    n, m = map(int, input().split())
    v = list(map(int, input().split()))
    p = 0
    d = []
    for u in v:
        p += u
        d.append(p)
    sections = [(list(g)) for k, g in groupby(v, key = lambda x: x < m) if not k] 
    best = 0
    for section in sections:
        if m not in section:
            continue
        parts = [(list(g)) for k, g in groupby(section, key = lambda x: x== m) if not k]
        if len(parts) == 1:
            best = max(best, sum(parts[0]))
        for i in range(len(parts)-1):
            best = max(best, sum(parts[i]) + sum(parts[i+1]))
    best += m
    print(best)
