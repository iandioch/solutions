def parse_route(rstr):
    d = []
    for step in rstr.split(','):
        d.append((step[0], int(step[1:])))
    return d

def get_visited(route):
    curr = (0, 0)
    for step in route:
        direction, distance = step
        change = (0, 0)
        if direction == 'R':
            change = (1, 0)
        elif direction == 'L':
            change = (-1, 0)
        elif direction == 'U':
            change = (0, -1)
        elif direction == 'D':
            change = (0, 1)
        else:
            print('Direction not recognised:', direction)
            return

        for _ in range(distance):
            curr = (curr[0] + change[0], curr[1] + change[1])
            yield curr

a = list(get_visited(parse_route(input())))
d = {}
curr = 0
for step in a:
    curr += 1
    if step in d:
        continue
    d[step] = curr

b = list(get_visited(parse_route(input())))
curr = 0
bestdist = 9999999999999
for step in b:
    curr += 1
    if step in d:
        bestdist = min(bestdist, d[step] + curr)

print(bestdist)
