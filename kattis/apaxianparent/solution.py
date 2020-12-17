def main():
    y, p = input().split()
    if y[-1] == 'e':
        print('{}x{}'.format(y, p))
    elif y[-1] in 'aeiou':
        print('{}ex{}'.format(y[:-1], p))
    elif y.endswith('ex'):
        print('{}{}'.format(y, p))
    else:
        print('{}ex{}'.format(y, p))

main()
