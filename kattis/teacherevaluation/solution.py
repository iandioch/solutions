n, p = map(int, input().split())
tot = sum(map(int, input().split()))

if p == 100:
    print('impossible')
else:
    ans = 0
    while tot/n < p:
        tot += 100
        n += 1
        ans += 1
    print(ans)
