while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    a, b = sorted([a, b])
    c, d = sorted([c, d])

    i = b*10 + a
    j = d*10 + c

    if i == j:
        print('Tie.')
    elif i == 21:
        print ('Player 1 wins.')
    elif j == 21:
        print('Player 2 wins.')
    elif a == b:
        if c == d:
            if a > c:
                print('Player 1 wins.')
            else:
                print('Player 2 wins.')
        else:
            print('Player 1 wins.')
    elif c == d:
        print('Player 2 wins.')
    else:
        if i > j:
            print('Player 1 wins.')
        else:
            print('Player 2 wins.')
