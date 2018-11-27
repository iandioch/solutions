n = int(input())
m = sorted([int(c) for c in input().split()])

ok = True
mmax = 1
for i in range(1, n+1):
    if m[i-1] > i:
        ok = False
        break
    mmax = min(mmax, m[i-1]/(i))

if ok:
    print(mmax)
else:
    print('impossible')
