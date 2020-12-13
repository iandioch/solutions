a, b, c = map(int, input().split())
a += b
tot = 0
while a >= c:
    a -= c
    tot += 1
    a += 1
print(tot)
