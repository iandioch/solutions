import sys
from collections import defaultdict

def replace(pairs, repl):
    out = defaultdict(int)
    for pair in pairs:
        a, b = pair
        out[a + repl[pair]] += pairs[pair]
        out[repl[pair] + b] += pairs[pair]
    return out
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

    pairs = defaultdict(int)
    for i in range(len(template)-1):
        pairs[template[i] + template[i+1]] += 1

    for i in range(1, 41):
        pairs = replace(pairs, repl)

    d = defaultdict(int)
    for pair in pairs:
        d[pair[0]] += pairs[pair]
        d[pair[1]] += pairs[pair]
    for c in d:
        d[c] //= 2
    d[template[0]] += 1
    d[template[-1]] += 1

    minc = min(d[c] for c in d)
    maxc = max(d[c] for c in d)
    print(maxc-minc)

main()
