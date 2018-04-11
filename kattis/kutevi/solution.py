from collections import deque

n, m = map(int, input().split())

poss = [False for _ in range(360)]

given = list(map(int, input().split()))
q = deque()
q.append(given[0])
while len(q):
    a = q.pop()
    if poss[a]:
        continue
    poss[a] = True
    for o in given:
        b = abs(a - o)
        if not poss[b]:
            q.append(b)
        c = (a+o)%360
        if not poss[c]:
            q.append(c)

for a in input().split():
    ok = poss[int(a)]
    if ok:
        print('YES')
    else:
        print('NO')
