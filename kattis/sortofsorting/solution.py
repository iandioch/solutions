while True:
    n = int(input())
    if n == 0:
        break
    s = [input() for _ in range(n)]
    s.sort(key=lambda x:x[0:2])
    print('\n'.join(s))
    print()
