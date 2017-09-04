num_trips = int(input())

d = {}
for i in range(num_trips):
    dest, year = input().split()
    if dest in d:
        d[dest].append(int(year))
    else:
        d[dest] = [int(year)]

for k in d:
    d[k] = sorted(d[k])

num_q = int(input())
for i in range(num_q):
    dest, t = input().split()
    print(d[dest][int(t)-1])
