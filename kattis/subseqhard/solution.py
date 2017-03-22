from collections import defaultdict

ntests = int(input())
for test in range(ntests):
    input(), input()
    m = map(int, input().split())
    d = defaultdict(lambda: 0)
    tot = 0
    ans = 0
    for v in m: 
        d[tot] += 1
        tot += v
        if tot - 47 in d:
            ans += d[tot-47]
    print(ans)
