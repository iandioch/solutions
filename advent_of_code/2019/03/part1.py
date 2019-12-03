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

a = set(get_visited(parse_route(input())))
b = set(get_visited(parse_route(input())))
bestdist = 9999999999999
for combo in a&b:
    d = abs(combo[0]) + abs(combo[1])
    if d < bestdist:
        bestdist = d

print(bestdist)
