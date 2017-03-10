n = int(input())

for i in range(n):
    m = int(input())
    v = list(map(int, input().split()))
    d = set()
    poss = set(v)
    for j in v.copy():
        if j in d:
            poss.remove(j)
            d.remove(j)
        d.add(j)
    print('Case #{}: {}'.format(i+1, poss.pop()))
