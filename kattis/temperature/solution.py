z, d = map(int, input().split())

if z == 0 and d == 1:
    print('ALL GOOD')
elif d == 1:
    print('IMPOSSIBLE')
else:
    print ('{:.7f}'.format(z/(1-d)))
