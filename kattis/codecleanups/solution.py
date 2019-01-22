def main():
    n = int(input())
    m = set(map(int, input().split()))

    dirtiness = 0
    bad_pushes = 0
    i = 1
    cleanups = 0

    while i <= 366:
        if dirtiness >= 20:
            dirtiness = 0
            bad_pushes = 0
            cleanups += 1
            i -= 1
            continue
        dirtiness += bad_pushes
        if i in m:
            bad_pushes += 1
        i += 1
    if dirtiness > 0:
        cleanups += 1
    print(cleanups)

if __name__ == '__main__':
    main()
