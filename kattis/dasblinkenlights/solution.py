def main():
    p, q, s = map(int, input().split())

    pset = set()
    qset = set()
    a = p
    while a <= s:
        pset.add(a)
        a += p
    a = q
    while a <= s:
        qset.add(a)
        a += q
    ans = (pset & qset)
    if len(ans):
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    main()
