def make_grid(cypher):
    used = set()
    alpha = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    out = []
    for c in [d for d in cypher if d in alpha] + list(alpha):
        if c in used:
            continue
        out.append(c)
        used.add(c)
    return [out[i*5:(i+1)*5] for i in range(5)]

def which_row(grid, c):
    for i in range(5):
        if c in grid[i]:
            return i

def which_column(grid, c):
    for y in range(5):
        for x in range(5):
            if grid[y][x] == c:
                return x

def main():
    cypher = input().upper()
    inp = [c for c in input().upper() if c!=' ']

    grid = make_grid(cypher)

    ans = []

    i = 0
    while i < len(inp):
        nexti = i+2
        if i+1 < len(inp):
            pair = [inp[i], inp[i+1]]
        else:
            pair = [inp[i], 'X']
        if pair[0] == pair[1]:
            pair[1] = 'X'
            nexti = i +1

        out = ['Q', 'Q']
        pos = [(which_column(grid, pair[0]), which_row(grid, pair[0])),
               (which_column(grid, pair[1]), which_row(grid, pair[1]))]
        if pos[0][1] == pos[1][1]:
            # same row
            out = [grid[pos[0][1]][(pos[0][0] + 1)%5], grid[pos[0][1]][(pos[1][0] + 1)%5]]
        elif pos[0][0] == pos[1][0]:
            # same column
            out = [
                grid[(pos[0][1]+1)%5][pos[0][0]],
                grid[(pos[1][1]+1)%5][pos[1][0]]
            ]
        else:
            out = [
                grid[pos[0][1]][pos[1][0]],
                grid[pos[1][1]][pos[0][0]]
            ]

        ans += out
        i = nexti
    print(''.join(ans))

main()
