size, num = map(int, input().split())
curr = 0
ans = 0
for _ in range(num):
    action, n = input().split()
    n = int(n)
    if action[0] == 'e':
        if curr + n > size:
            ans += 1
        else:
            curr += n
    else:
        curr -= n
print(ans)
