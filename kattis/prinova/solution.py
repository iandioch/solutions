n = int(input())
d = sorted(map(int, input().split()))
a, b = map(int, input().split())

def find_nearest(v):
    be = v
    bd = 10000000000
    for c in d:
        if abs(v-c) < bd:
            bd = abs(v-c)
            be = c
    return be

best = -1
bestdiff = 0
a2 = a
b2 = b
if a % 2 == 0:
    a2 += 1
if b % 2 == 0:
    b2 -= 1
best = a2
bestdiff = abs(find_nearest(a2)-a2)
bdiff = abs(find_nearest(b2)-b2)
if bdiff > bestdiff:
    bestdiff = bdiff
    best = b2

for i in range(n-1):
    num = (d[i+1] + d[i])//2
    if num % 2 == 0:
        num -= 1
    if num < a:
        continue
    if num > b:
        break
    diff = abs(num - d[i])
    if diff > bestdiff:
        bestdiff = diff
        best = num

print(best)
        
