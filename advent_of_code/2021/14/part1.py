import sys
from collections import defaultdict

def replace(template, pairs):
    betweens = []
    for i in range(len(template)-1):
        k = template[i] + template[i+1]
        if k in pairs:
            betweens.append(pairs[k])
        else:
            betweens.append(None)
    out = []
    for a, b in zip(template, betweens):
        out.append(a)
        if b is not None:
            out.append(b)
    out.append(template[-1])
    return ''.join(out)

def main():
    template = input()
    input()
    repl = {}
    for line in sys.stdin.readlines():
        inp, out = line.strip().split(' -> ')
        repl[inp] = out

    print('initial', template)
    for i in range(1, 11):
        template = replace(template, repl)
        print('after step', i, len(template))

    d = defaultdict(int)
    for c in template:
        d[c] += 1
    minc = min(d[c] for c in d)
    maxc = max(d[c] for c in d)
    print(maxc - minc)

main()
