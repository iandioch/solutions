def check(s):
    tot = 0
    for i in range(1, len(s) + 1):
        v = s[len(s) - i]
        if i % 2 == 0:
            v *= 2
            if v >= 10:
                v = (v//10) + (v%10)
        tot += v
    return tot % 10 == 0

t = int(input())
for _ in range(t):
    s = [int(c) for c in input()]
    print(['FAIL', 'PASS'][check(s)])
