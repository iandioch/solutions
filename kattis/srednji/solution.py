from collections import defaultdict
n, k = map(int, input().split())
ns = list(map(int, input().split()))

r = []
ki = -1
for i, v in enumerate(ns):
    if v == k:
        r.append(0)
        ki = i
    elif v < k:
        r.append(-1)
    else:
        r.append(1)

tot = 0
cnt = defaultdict(int)
for i in range(ki, n):
    tot += r[i]
    cnt[tot] += 1

ans = 0
tot = 0
for i in range(ki, -1, -1):
    tot += r[i]
    ans += cnt[-tot]

print(ans)
