n = int(input())
v = list(map(lambda x: 1 if x == 'M' else -1, input()))

curr = 0
ans = 0
while ans < len(v)-1:
    if abs(curr + v[ans+1]) < abs(curr + v[ans]):
        v[ans], v[ans+1] = v[ans+1], v[ans]
    if abs(curr + v[ans]) > n:
        break
    curr += v[ans]
    ans += 1
if abs(curr + v[ans]) <= n:
    ans += 1

print(ans)
