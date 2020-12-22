def main():
    import sys
    from collections import defaultdict
    frosh = defaultdict(int)

    n = int(sys.stdin.readline())
    for line in sys.stdin.readlines():
        line = tuple(sorted(line.strip().split()))
        frosh[line] += 1
    maxn = max(frosh[x] for x in frosh)
    print(sum(frosh[y] for y in frosh if frosh[y] == maxn))

main()
