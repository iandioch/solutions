s = list("abcdefghijklmnop")

orders = input().split(',')

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

print(''.join(s))
