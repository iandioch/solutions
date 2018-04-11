from math import ceil
b, k, g = map(int, input().split())
gr = k//g
ans = 0
while b > 1:
    b -= gr
    ans += 1
print(ans)
