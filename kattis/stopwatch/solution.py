n = int(input())
on = False
prev = 0
ans = 0
for _ in range(n):
    t = int(input())

    if on:
        ans += t-prev

    on = not on
    prev = t

if on:
    print('still running')
else:
    print(ans)
