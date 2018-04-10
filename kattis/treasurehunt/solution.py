r, c = map(int, input().split())

rows = [input().strip() for _ in range(r)]

visited = set()
x, y = 0, 0
curr = 0
while True:
    if y >= r or x >= c or x < 0 or y < 0:
        print('Out')
        break

    if (x,y) in visited:
        print('Lost')
        break
    visited.add((x,y))

    d = rows[y][x]
    if d == 'T':
        print(curr)
        break

    curr += 1
    if d == 'N':
        y -= 1
    elif d == 'S':
        y += 1
    elif d == 'W':
        x -= 1
    elif d == 'E':
        x += 1
