ORDER = {
    'upper': '3',
    'middle': '2',
    'lower': '1',
}

t = int(input())
for _ in range(t):
    n = int(input())
    d = []
    longest = 0
    for _ in range(n):
        s = input().split(':')
        name = s[0]
        p = s[1].strip().split()[0].split('-')
        d.append(([ORDER[c] for c in p], name))
        longest = max(longest, len(p))
    for i in range(n):
        name = d[i][1]
        v = d[i][0][::-1]
        while len(v) < 10:
            v = v + [ORDER['middle']]
        d[i] = (v, name)
    d.sort(key=lambda x:x[1])
    d.sort(key=lambda x:x[0], reverse=True)
    print('\n'.join(c[1] for c in d))
    print('==============================')
