ntests = int(input())

for test in range(ntests):
    n = int(input())
    nums = sorted([input() for _ in range(n)], key=len, reverse=True)
    d = set()
    ok = True
    for num in nums:
        if not ok:
            continue
        if num in d:
            ok = False
            continue
        for i in range(1, len(num)+1):
            d.add(num[:i])
    if ok:
        print('YES')
    else:
        print('NO')
