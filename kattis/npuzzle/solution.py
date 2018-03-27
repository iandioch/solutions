des = ['ABCD', 'EFGH', 'IJKL', 'MNO.']
d = {}
for i in range(4):
    for j in range(4):
        c = des[i][j]
        d[c] = (i, j)

a = 0
for i in range(4):
    s = input()
    for j in range(4):
        c = s[j]
        if c == '.':
            continue
        e = d[c]
        b = abs(i-e[0]) + abs(j-e[1])
        a += b
print(a)
