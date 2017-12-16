s = list("abcdefghijklmnop")

orders = input().split(',')
d = set()
v = []

for _ in range(1000000000):
    for o in orders:
        op = o[0]
        if op == 's':
            a = int(o[1:])
            s = s[-a:] + s[:-a] 
            continue
        if op == 'x':
            a,b = map(int, o[1:].split('/'))
            s[a], s[b] = s[b], s[a]
        if op == 'p':
            a,b = map(s.index, o[1:].split('/'))
            s[a], s[b] = s[b], s[a]
    t = tuple(s)
    if t in d:
        break
    d.add(t)
    v.append(t)

print(''.join(v[((10**9)%len(v))-1]))
