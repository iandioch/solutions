n = int(input())
ans = 1
for m in range(int(n**(1/9.0)) + 1, 0, -1):
    if n % m**9 == 0:
        ans = m
        break

print(ans)
