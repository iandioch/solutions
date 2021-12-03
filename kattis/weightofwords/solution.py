ALPHA = 'abcdefghijklmnopqrstuvwxyz'
L, W = map(int, input().split())
ans = []
poss = True
for remaining in range(L, 0, -1):
    leeway = W - remaining + 1
    if leeway <= 0:
        poss = False
        break
    a = min(leeway, 26)
    W -= a
    ans.append(a)


if (not poss) or (W > 0) or (len(ans) != L):
    print('impossible')
else:
    print(''.join(ALPHA[c-1] for c in ans))
