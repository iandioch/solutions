s = input()
n = len(s)//3
out = []
for i in range(n):
    x = [s[i], s[i+n], s[i+n+n]]
    out.append(sorted(x)[1])
print(''.join(out))
