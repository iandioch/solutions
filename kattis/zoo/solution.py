listnum = 1
while True:
    d = {}
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        s = input().split()[-1].lower()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    print('List {}:'.format(listnum))
    for a in sorted(d.keys()):
        print(a, '|', d[a])
    listnum += 1
