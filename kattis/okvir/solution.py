m, w = map(int, input().split())

u, l, r, d = map(int, input().split())

words = [input().strip() for _ in range(m)]

a, b = '#', '.'
n = 0
for i in range(u):
    for j in range(w+l+r):
        if (n+j)%2 == 0:
            print(a, end='')
        else:
            print(b, end='')
    print()
    n += 1

for i in range(m):
    for j in range(l):
        if (n+j)%2 == 0:
            print(a, end='')
        else:
            print(b, end='')
    print(words[i], end='')
    for j in range(l+w, l+w+r):
        if (n+j)%2 == 0:
            print(a, end='')
        else:
            print(b, end='')
    print()
    n += 1

for i in range(d):
    for j in range(w+l+r):
        if (n+j)%2 == 0:
            print(a, end='')
        else:
            print(b, end='')
    print()
    n += 1
