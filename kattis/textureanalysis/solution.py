i = 1
while True:
    s = input().strip()
    if s == 'END':
        break

    u = s.split('*')
    if len(u) > 2:
        u = u[1:-1]
    if len(set(u)) != 1:
        print(i, 'NOT EVEN')
    else:
        print(i, 'EVEN')
    i += 1
