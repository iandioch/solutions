def main():
    n = int(raw_input())
    m = sorted(map(int, (raw_input() for _ in range(n))))
    seen = set()
    seen.add(0)
    best = 0
    bestdiff = 1000
    for i in m:
        for o in list(seen):
            d = abs(1000 - (i+o))
            if d == bestdiff and best < (i+o):
                best = (i+o)
            elif d < bestdiff:
                best = (i+o)
                bestdiff = d
            if d > bestdiff and (i+o) > 1000:
                continue
            seen.add(i+o)
    print(best)

main()
