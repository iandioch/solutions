n = int(input())
names = [input() for _ in range(n)]

if sorted(names) == names:
    print('INCREASING')
elif sorted(names, reverse=True) == names:
    print('DECREASING')
else:
    print('NEITHER')
