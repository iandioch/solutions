def main():
    n = int(input())

    lo = 1
    hi = 10

    while hi - lo > 0.00000001:
        mid = lo + (hi-lo)/2
        midn = mid**mid
        if midn > n:
            hi = mid
        else:
            lo = mid

    print(lo)

main()
