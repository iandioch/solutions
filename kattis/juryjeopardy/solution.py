def walk(x, y, direction):
    if direction == 0:
        x += 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x -= 1
    else:
        y -= 1
    return (x, y)

def run(s):
    d = 0
    x, y = 0, 0
    path = set([(x,y)])
    minx = 0
    maxx = 0
    miny = 0
    maxy = 0
    for c in s:
        if c == 'F':
            x, y = walk(x, y, d)
        elif c == 'R':
            d += 1
            d %= 4
            x, y = walk(x, y, d)
        elif c == 'L':
            d -= 1
            if d < 0:
                d += 4
            x, y = walk(x, y, d)
        elif c == 'B':
            d += 2
            d %= 4
            x, y = walk(x, y, d)
        path.add((x,y))
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)
    h = maxy - miny + 1 + 2
    w = maxx - minx + 1 + 1

    print(h, w)
    print('#'*w)
    for j in range(miny, maxy+1):
        for i in range(minx, maxx+1):
            if (i,j) in path:
                print('.', end='')
            else:
                print('#', end='')
        print('#')
    print('#'*w)

n = int(input())
print(n)

for _ in range(n):
    run(input())
