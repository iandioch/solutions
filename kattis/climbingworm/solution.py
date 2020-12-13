a, b, h = map(int, input().split())

ans = 0
c = 0
while True:
    ans += 1
    c += a
    if c >= h:
        break
    c -= b
print(ans)
