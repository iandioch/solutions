import sys

lines = [s.strip() for s in sys.stdin.readlines()]
blocked = [[c == '.' for c in line] for line in lines]
alive = [[1 if c == '#' else 0 for c in line] for line in lines]
HEIGHT = len(lines)
WIDTH = len(lines[0])
DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]

def step(inp):
    tot = [[0 for _ in range(WIDTH + 1)] for _ in range(HEIGHT + 1)]
    out = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for y in range(HEIGHT):
        for x in range(WIDTH):
            out[y][x] = inp[y][x]
            if blocked[y][x]:
                continue
            num_neighbours = 0
            for d in DIRS:
                dist = 1
                while True:
                    j = y + d[0]*dist
                    i = x + d[1]*dist
                    if j < 0 or j >= HEIGHT or i < 0 or i >= WIDTH:
                        break
                    if not blocked[j][i]:
                        num_neighbours += inp[j][i]
                        break
                    dist += 1
            if inp[y][x] == 0 and num_neighbours == 0:
                out[y][x] = 1
            elif inp[y][x] == 1 and num_neighbours >= 5:
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
