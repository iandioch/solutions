def get_max(a, b, c, d):
    a, b, c = sorted([a, b, c])
    i = 0
    ans = a*a + b*b + (c+d)*(c+d) + 7*a
    while d != 0 and i < 100:
        a += 1
        d -= 1
        a, b, c = sorted([a, b, c])
        v = a*a + b*b + (c+d)*(c+d) + 7*a
        ans = max(ans, v)
        i += 1
    return ans


n = int(input())
for _ in range(n):
    print(get_max(*map(int, input().split())))
