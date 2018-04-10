from collections import defaultdict

def coord_to_str(x, y):
    return chr(x + ord('a')) + str(y)

ORDER = 'KQRBN'
black = defaultdict(list)
white = defaultdict(list)

bp = []
wp = []

for j in range(8, 0, -1):
    input()
    p = input().split('|')
    for i, c in enumerate(p[1:9]):
        c = c.strip('.:')
        if len(c) and c.upper() in 'KQRBNP':
            if c.lower() == c:
                # black
                if c == 'p':
                    bp.append((i,j))
                else:
                    black[c.upper()].append((i, j))
            else:
                # white
                if c == 'P':
                    wp.append((i,j))
                else:
                    white[c].append((i, j))
input()

bp.sort(key = lambda x:(-x[1], x[0]))
wp.sort(key = lambda x:x[::-1])

for k in black:
    black[k].sort(key = lambda x:(-x[1], x[0]))
for k in white:
    white[k].sort(key = lambda x:x[::-1])

s = 'White: '
for o in ORDER:
    if o in white:
        for g in white[o]:
            s += o + coord_to_str(*g) + ','
for p in wp:
    s += coord_to_str(*p) + ','
print(s.strip(','))

s = 'Black: '
for o in ORDER:
    if o in black:
        for g in black[o]:
            s += o + coord_to_str(*g) + ','
for p in bp:
    s += coord_to_str(*p) + ','
print(s.strip(','))
