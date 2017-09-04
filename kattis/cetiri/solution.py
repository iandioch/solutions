n = sorted(list(map(int, input().split())))

if n[2] - n[1] == n[1] - n[0]:
    # goes before or after
    print(n[2] + abs(n[2]-n[1]))
elif n[2] - n[1] > n[1] - n[0]:
    # goes between 1 and 2
    print(n[1] + abs(n[1]-n[0]))
else:
    # goes between 0 and 1
    print(n[0] + abs(n[2]-n[1]))
