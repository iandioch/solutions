num_player, req_points, num_lines = map(int, input().split())
player = {input():0 for _ in range(num_player)}

winners = []
for _ in range(num_lines):
    name, points = input().split()
    points = int(points)
    player[name] += points
    if player[name] >= req_points:
        winners.append(name)

if len(winners):
    dset = set()
    for name in winners:
        if name in dset:
            continue
        dset.add(name)
        print('{} wins!'.format(name))
else:
    print('No winner!')
