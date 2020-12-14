import sys
from collections import defaultdict

# Map a mask like 001X0 to a generator yielding:
# [None, None, 1, 0, None],
# [None, None, 1, 1, None]
# Where None is a no-op 'bit', and a 0 or 1 should be written directly to the
# address.
def get_masks(orig, i=0):
    if i >= len(orig):
        yield []
    elif orig[i] == 'X':
        rest = list(get_masks(orig, i+1))
        yield from [[0] + r for r in rest]
        yield from [[1] + r for r in rest]
    else:
        yield from ([None if orig[i] == '0' else 1] + r for r in list(get_masks(orig, i+1)))

# Apply all the masks in the masks list to the list 'val'.
def apply_mask(masks, val):
    for mask in masks:
        yield [vc if mc == None else mc for vc, mc in zip(val, mask)]

def main():
    mem = defaultdict(int)
    mask = [[None]*36] # no-op mask to start off with
    for line in sys.stdin.readlines():
        p = line.split('=')
        if p[0].strip() == 'mask':
            orig_mask = p[1].strip()
            mask = list(get_masks(orig_mask))
            continue

        addr = bin(int(p[0].strip()[4:-1]))[2:].zfill(len(mask[0]))
        addrs = apply_mask(mask, addr)
        val = int(p[1].strip())
        for a in addrs:
            a = int(''.join(str(c) for c in a), 2) # map list of ints to int
            mem[a] = val

    print(sum(mem[addr] for addr in mem))

main()
