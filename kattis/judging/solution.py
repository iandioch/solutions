n = int(input())
d = {}
for i in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
e = {}
for i in range(n):
    s = input()
    if s in e:
        e[s] += 1
    else:
        e[s] = 1

ans = 0
for k in d:
    if k not in e:
        continue
    ans += min(d[k], e[k])
print(ans)
