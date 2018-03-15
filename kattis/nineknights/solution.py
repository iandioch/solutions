g = [[True if x == 'k' else False for x in input()] for _ in range(5)]
ok = True

def check(i, j):
    global ok
    if i >= 5 or j >= 5:
        return
    if i < 0 or j < 0:
        return
    if g[i][j]:
        ok = False

tot = 0
for x in range(5):
    for y in range(5):
        if not g[x][y]:
            continue
        tot += 1
        check(x+2, y+1)
        check(x+1, y+2)
        check(x-2, y+1)
        check(x-1, y+2)
        check(x+2, y-1)
        check(x+1, y-2)
        check(x-2, y-1)
        check(x-1, y-2)

if ok and tot == 9:
    print('valid')
else:
    print('invalid')

