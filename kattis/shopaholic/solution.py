n = int(input())
v = sorted(map(int, input().split()), reverse=True)
ans = 0
for i in range(2, len(v), 3):
    ans += v[i]
print(ans)
