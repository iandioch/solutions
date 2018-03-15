y, x = map(int, input().split())
d = [[True if c == '#' else False for c in input()] for _ in range(y)]
col = [[None for _ in range(x)] for _ in range(y)]

maxcol = 0

def flood(i, j, colour):
    if i < 0 or j < 0 or i >= x or j >= y:
        return
    if not d[j][i]:
        return
    if col[j][i]:
        return
    col[j][i] = colour
    flood(i+1, j, colour)
    flood(i+1, j-1, colour)
    flood(i+1, j+1, colour)
    flood(i, j-1, colour)
    flood(i, j+1, colour)
    flood(i-1, j, colour)
    flood(i-1, j-1, colour)
    flood(i-1, j+1, colour)

for i in range(x):
    for j in range(y):
        if d[j][i] and not col[j][i]:
            maxcol += 1
            flood(i, j, maxcol)

print(maxcol)
