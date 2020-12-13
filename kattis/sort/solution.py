def main():
    from collections import defaultdict
    n, c = map(int, input().split())
    counts = defaultdict(int)
    nums = map(int, input().split())

    seen_order = []
    seenset = set()
    for num in nums:
        counts[num] += 1
        if num not in seenset:
            seen_order.append(num)
        seenset.add(num)

    ans = list(seen_order)
    ans.sort(key = lambda x: counts[x], reverse=True)

    outp = []
    for n in ans:
        for c in range(counts[n]):
            outp.append(n)

    print(' '.join(map(str, outp)))
    #print('{} '.format(n)*counts[n], end='')

main()
