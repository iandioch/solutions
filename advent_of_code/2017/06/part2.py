d = list(map(int, input().split()))

configs = {}
while True:
    if tuple(d) in configs:
        print(len(configs) - configs[tuple(d)])
        break

    configs[tuple(d)] = len(configs)
    index = 0
    most = 0
    for i in range(len(d)):
        if d[i] > most:
            most = d[i]
            index = i

    d[index] = 0
    while most > 0:
        index = (index + 1) % len(d)
        d[index] += 1
        most -= 1
