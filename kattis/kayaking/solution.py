def main():
    allg = list(map(int, raw_input().split()))
    speed = list(map(int, raw_input().split()))
    cval = list(map(int, raw_input().split()))
    cval = sorted(cval)
    #p = ([na]*a) + ([nb]*b) + ([nc]*c)

    def is_poss(val):
        #print('Is_poss:', val)
        used = [False for _ in range(len(cval))]
        g = allg[:]
        #[a, b, c] speed = [na, nb, nc]
        for i in range(3):
            if g[i] == 0:
                continue
            for j in range(i, 3):
                for boat, boatspeed in enumerate(cval):
                    if used[boat]:
                        continue
                    if g[i] == 0 or g[j] == 0:
                        continue
                    if i == j and g[i] < 2:
                        continue
                    x = boatspeed*(speed[i] + speed[j])
                    if x < val:
                        continue
                    #print('Putting', i, j, 'in boat', boat)
                    used[boat] = True
                    g[i] -= 1
                    g[j] -= 1
        #print('All allocated?', sum(g) == 0)
        return sum(g) == 0

    lo = 1
    #cval[0]*(p[0] + p[1])
    hi = 10000000#cval[-1]*(p[-2] + p[-1])

    while hi- lo > 1:
        mid = lo + (hi-lo)//2
        #print(lo, mid, hi)
        if is_poss(mid):
            lo = mid
        else:
            hi = mid-1
    #print('done', lo, hi)
    if is_poss(hi):
        print(hi)
    else:
        print(lo)


main()
