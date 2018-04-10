while True:
    n, m = map(int, raw_input().split())
    if n == m == 0:
        break

    calls = []
    for _ in range(n):
        src, dest, start, dur = map(int, raw_input().split())
        calls.append((start, start + dur))

    for _ in range(m):
        start, dur = map(int, raw_input().split())
        end = start + dur
        ans = 0
        for a, b in calls:
            if (a <= start and b > start) or (a < end and b > end) or (a >= start and b <= end):
                ans += 1
        print(ans)

