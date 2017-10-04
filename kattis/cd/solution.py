while True:
    n, m = map(int, raw_input().split())
    if n == 0 and m == 0:
        break
    a = set(int(raw_input()) for _ in range(n))
    ans = 0
    for _ in range(m):
        if int(raw_input()) in a:
            ans += 1
    print(ans)
