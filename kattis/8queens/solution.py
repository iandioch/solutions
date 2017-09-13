queens = set()
rows = set()
cols = set()
g = [input() for _ in range(8)]
ok = True
for row in range(8):
    for column in range(8):
        if g[row][column] == '*':
            for i in range(8):
                if (row-i, column-i) in queens:
                    ok = False
                    break
                if (row+i, column+i) in queens:
                    ok = False
                    break
                if (row-i, column+i) in queens:
                    ok = False
                    break
                if (row+i, column-i) in queens:
                    ok = False
                    break
            if row in rows or column in cols:
                ok = False
                break
            rows.add(row)
            cols.add(column)
            queens.add((row, column))
    if not ok:
        break

if ok and len(queens) == 8:
    print('valid')
else:
    print('invalid')
