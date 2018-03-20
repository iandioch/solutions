n = int(input())
s = sorted(map(int, input().split()))
ok = False
for i in range(n-2):
    if s[i] + s[i+1] > s[i+2]:
        ok = True
        break
if ok:
    print('possible')
else:
    print('impossible')
