alpha = 'abcdefghijklmnopqrstuvwxyz'.upper()
d = {a:alpha.index(a) for a in alpha}

encrypted = input()
key = input()

ans = ''
for i, c in enumerate(encrypted):
    opp = -1 if (i%2 == 0) else 1
    a = alpha[(d[c] + opp*d[key[i]]) % len(alpha)]
    ans += a

print(ans)
