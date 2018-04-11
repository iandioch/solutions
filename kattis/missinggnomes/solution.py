n, m = map(int, input().split())

given = [int(input()) for _ in range(m)]
given_set = set(given)
todo = [i for i in range(1, n+1) if i not in given_set]

i, j = 0, 0

while i < m and j < len(todo):
    a = given[i]
    b = todo[j]
    if a < b:
        print(a)
        i += 1
    else:
        print(b)
        j += 1

while i < m:
    print(given[i])
    i += 1

while j < len(todo):
    print(todo[j])
    j += 1

