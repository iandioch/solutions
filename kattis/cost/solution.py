import heapq

NOT_FOUND = 11111111111

num_langs, num_trans = map(int, input().split())
langs = input().split() + ['English']
trans_lang = {n:set() for n in langs}
trans_cost = {n:{} for n in langs}
for _ in range(num_trans):
    a, b, c = input().split()
    c = int(c)
    trans_lang[a].add(b)
    trans_lang[b].add(a)
    trans_cost[a][b] = min(trans_cost[a].get(b, c), c)
    trans_cost[b][a] = min(trans_cost[b].get(a, c), c)
d = {n:NOT_FOUND for n in langs} # num steps
e = {n:NOT_FOUND for n in langs} # cost

q = []
heapq.heappush(q,(0, 0, 'English'))
while len(q):
    steps, cost, curr = heapq.heappop(q)
    if d[curr] < steps:
        continue
    if e[curr] <= cost:
        continue
    d[curr] = steps
    e[curr] = cost
    for other in trans_lang[curr]:
        tcost = trans_cost[curr][other]
        if steps+1 <= d[other]:
            heapq.heappush(q, (steps+1,tcost,other))

tot = 0
found_all = True
for lang in e:
    if e[lang] == NOT_FOUND:
        found_all = False
        break
    tot += e[lang]
if found_all:
    print(tot)
else:
    print('Impossible')
