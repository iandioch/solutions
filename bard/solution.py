def main():
    n = int(input()) # bard = 1
    e = int(input()) # number of evenings

    known = {i: set() for i in range(1, n+1)}

    song = 0

    for _ in range(e):
        m, *t = map(int, input().split())
        t = set(t)
        if 1 in t:
            # new song!
            for k in t:
                known[k].add(song)
            song += 1
        else:
            # sharing songs
            k = set()
            for s in t:
                k |= known[s]
            for s in t:
                known[s] = set(k)

    t = sorted(i for i in known if len(known[i]) == song)
    print('\n'.join(str(s) for s in t))

if __name__ == '__main__':
    main()
