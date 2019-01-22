def main():
    ncards = int(input())
    nturns = int(input())
    from collections import defaultdict

    d = defaultdict(set)
    predone = 0
    for _ in range(nturns):
        p, q, a, b = input().split()
        p = int(p)
        q = int(q)
        d[a].add(p)
        d[b].add(q)
        if a == b:
            predone += 1
            if a in d:
                del d[a]
    known = 0
    half_known = 0
    for e in d:
        if len(d[e]) == 2:
            known += 1
        if len(d[e]) == 1:
            half_known += 1
    unknown = ncards - (predone*2) - (known*2) - half_known
    ans = known
    if half_known == unknown:
        ans += half_known
    elif unknown == 2:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
