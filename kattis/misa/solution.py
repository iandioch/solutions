h, w = map(int, input().split())
lines = [[c == 'o' for c in input()] for _ in range(h)]

best = 0
tot = 0
for y in range(h):
    above = y > 0
    below = y < h-1
    for x in range(w):
        c = 0
        if x < w-1:
            if above and lines[y-1][x+1]:
                c += 1
            if lines[y][x+1]:
                c += 1
            if below and lines[y+1][x+1]:
                c += 1
        if x > 0:
            if above and lines[y-1][x-1]:
                c += 1
            if lines[y][x-1]:
                c += 1
            if below and lines[y+1][x-1]:
                c += 1
        if above and lines[y-1][x]:
            c += 1
        if below and lines[y+1][x]:
            c += 1
        if lines[y][x]:
            tot += c
        elif c > best:
            best = c

tot += best*2

print(tot//2)
