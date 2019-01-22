def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a, b = map(int, input().split())
    req = max(a, b//2+1)
    tot = 0
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:
                    print(a+b+c+d, end=' ')
                    tot += 1
                    if tot >= req:
                        print()
                        return


if __name__ == '__main__':
    main()
