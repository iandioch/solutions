def count(s):
    NUMS = set('0123456789')
    q = 0
    v = None
    from collections import defaultdict
    d = defaultdict(int)
    for c in s:
        if c not in NUMS:
            if v is not None:
                d[v] += max(q, 1)
            v = c
            q = 0
        else:
            q *= 10
            q += int(c)
    d[v] += max(q, 1)
    return d

def main():
    have, quant = input().split()
    quant = int(quant)
    want = input()
    haved = count(have)
    wantd = count(want)

    for c in wantd:
        if haved[c] == 0:
            print(0)
            return
        haved[c]*= quant
    print(min(haved[molecule]//(wantd[molecule]) for molecule in wantd))

main()
