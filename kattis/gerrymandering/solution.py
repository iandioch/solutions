def main():
    import sys
    read = sys.stdin.readline

    prec, dist = map(int, read().split())

    dists_a = [0 for _ in range(dist)]
    dists_b = [0 for _ in range(dist)]
    for _ in range(prec):
        d, a, b = map(int, read().split())
        dists_a[d-1] += a
        dists_b[d-1] += b

    wasted_a = 0
    wasted_b = 0
    tot_votes = 0
    for d in range(dist):
        a = dists_a[d]
        b = dists_b[d]
        tot = a+b
        req = tot//2 + 1
        tot_votes += tot 
        if a > b:
            wasted_a += (a - req)
            wasted_b += b
            print('A', a - req, b)
        else:
            wasted_a += a
            wasted_b += (b - req)
            print('B', a, b - req)

    print(abs(wasted_a - wasted_b) / tot_votes)

main()
