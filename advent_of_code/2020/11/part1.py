import sys

lines = [s.strip() for s in sys.stdin.readlines()]
blocked = [[c == '.' for c in line] for line in lines]
alive = [[1 if c == '#' else 0 for c in line] for line in lines]
HEIGHT = len(lines)
WIDTH = len(lines[0])

def step(inp):
    tot = [[0 for _ in range(WIDTH + 1)] for _ in range(HEIGHT + 1)]
    out = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    """tot[0][0] = inp[0][0]
    for y in range(1, HEIGHT):
        tot[y][0] = tot[y-1][0] + inp[y][0]
    for x in range(1, WIDTH):
        tot[0][x] = tot[0][x-1] + inp[0][x]
    for y in range(1, HEIGHT):
        for x in range(1, WIDTH):
            tot[y][x] = tot[y-1][x] + tot[y][x-1] - tot[y-1][x-1]# + inp[y][x]"""

    for y in range(HEIGHT):
        for x in range(WIDTH):
            out[y][x] = inp[y][x]
            if blocked[y][x]:
                continue
            num_neighbours = 0 #tot[y+1][x+1] - tot[y-2][x+1] - tot[y+1][x-2] + tot[y-2][x-2]
            for i in range(-1, 2):
                if x + i < 0 or x + i >= WIDTH:
                    continue
                for j in range(-1, 2):
                    if y + j < 0 or y + j >= HEIGHT:
                        continue
                    if i == j == 0:
                        continue
                    num_neighbours += inp[y+j][x+i]
            if inp[y][x] == 0 and num_neighbours == 0:
                out[y][x] = 1
            elif inp[y][x] == 1 and num_neighbours >= 4:
                out[y][x] = 0

    return out

def render(inp):
    print('-'*(WIDTH+2))
    for y in range(HEIGHT):
        s = ['|']
        for x in range(WIDTH):
            if blocked[y][x]:
                s.append('.')
            else:
                s.append('L#'[inp[y][x]])
        s.append('|')
        print(''.join(s))
    print('-'*(WIDTH+2))

i = 1
while True:
    print('Before step #', i)
    #render(alive)
    new_alive = step(alive)
    if new_alive == alive:
        print('no change!')
        break
    alive = new_alive
    print('End of step #', i)
    i += 1

render(alive)
print(sum(sum(c) for c in alive))
