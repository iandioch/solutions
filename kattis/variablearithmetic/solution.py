v = {}

while True:
    s = input()
    if s == '0':
        break
    p = s.split()
    if len(p) > 2 and p[1] == '=':
        var = p[0]
        value = int(p[2])
        v[var] = value
        continue

    i = 0
    ans = 0
    q = []
    while i < len(p):
        if p[i] in v:
            ans += v[p[i]]
        elif p[i].isdigit():
            ans += int(p[i])
        else:
            q.append(p[i])
        i += 2
    s = ''
    if ans != 0:
        s = '{}'.format(ans)
    for var in q:
        s += ' + {}'.format(var)
    s = s.strip()
    s = s.strip('+')
    s = s.strip()
    print(s)
