d = {}
e = {}

n = int(input())
for _ in range(n):
    who, first, other = input().split()
    first, other = float(first), float(other)
    d[who] = other
    e[who] = first

s = sorted(d, key = lambda x:d[x])

best_time = e[s[-1]]*4
best_team = []
for c in s:
    team = [c]
    time = e[c]
    for o in s:
        if c == o:
            continue
        team.append(o)
        time += d[o]
        if len(team) == 4:
            break
    if time < best_time:
        best_time = time
        best_team = team
print('{:.9f}'.format(best_time))
print('\n'.join(best_team))
