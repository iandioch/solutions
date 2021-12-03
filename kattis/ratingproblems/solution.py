n, k = map(int, input().split())
tot = sum(int(input()) for _ in range(k))
print((tot -3*(n-k))/n, (tot +3*(n-k))/n)
