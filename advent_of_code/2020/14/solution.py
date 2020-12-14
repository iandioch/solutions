import sys
from collections import defaultdict

def apply_mask(mask, val):
    return [vc if mc == 'X' else mc for vc, mc in zip(val, mask)]

def main():
    mem = defaultdict(int)
    mask = 'X'*36
    for line in sys.stdin.readlines():
        p = line.split('=')
        if p[0].strip() == 'mask':
            mask = p[1].strip()
            continue
        addr = int(p[0].strip()[4:-1])
        val = bin(int(p[1].strip()))[2:].zfill(len(mask))

        out = apply_mask(mask, val)
        mem[addr] = out

    print(sum(int(''.join(mem[addr]), 2) for addr in mem))

main()
