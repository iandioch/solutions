p, n = map(int, input().split())

r = set()
ans = - 1
for i in range(1, n+1):
    s = input().strip()
    r.add(s)
    if len(r) == p and ans < 0:
        ans = i
if ans < 0:
    print('paradox avoided')
else:
    print(ans)
