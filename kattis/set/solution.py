def valid3(a, b, c):
    same = 0
    diff = 0
    for i in range(4):
        if a[i] == b[i] and a[i] == c[i]:
            same += 1
        if a[i] != b[i] and a[i] != c[i] and b[i] != c[i]:
            diff += 1
    return same + diff == 4

cards = []
for i in range(4):
    s = input().split()
    for c in s:
        cards.append(c)

n = 0
for i in range(10):
    for j in range(i+1, 11):
        for k in range(j+1, 12):
            if valid3(cards[i], cards[j], cards[k]):
                print(i+1, j+1, k+1)
                n += 1

if n == 0:
    print('no sets')
