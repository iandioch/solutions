s = input().strip() + '+'
ans = 0

curr = 0
sign = 1
for c in s:
    if c in '-+':
        ans += sign*curr
        curr = 0
    if c == '-':
        sign = -1
    elif c == '+':
        sign = 1
    curr = curr*10 + (ord(c) - ord('0'))
print(ans)
