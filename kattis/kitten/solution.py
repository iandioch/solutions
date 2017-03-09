d = {}

k = int(input())

while True:
    p = list(map(int, input().split()))
    if len(p) == 1:
        break
    for j in p[1:]:
        d[j] = p[0]

while True:
    print(k, end=' ')
    if k in d:
        k = d[k]
    else:
        print()
        break
