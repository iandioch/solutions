import sys
import itertools

def parse_value(astr, i):
    if astr[i] == '[':
        i += 1# consume [
    else:
        ns = []
        while i < len(astr):
            if astr[i] == ']' or astr[i] == ',':
                break
            ns.append(astr[i])
            i += 1
        return int(''.join(ns)), i
    curr = []
    while i < len(astr):
        c = astr[i]
        if c == ']':
            return curr, i
        elif c == '[':
            sublist, j = parse_value(astr, i)
            curr.append(sublist)
            i = j+1
            continue
        elif c == ',':
            pass
        else:
            sub, j = parse_value(astr, i)
            i = j
            curr.append(sub)
            continue
        i += 1

def parse(astr, i):
    return parse_value(astr, 0)

LESS = 'LESS'
EQUAL = 'EQUAL'
GREATER = 'GREATER'

def compare(a, b, indent):
    lint = isinstance(a, int)
    rint = isinstance(b, int)
    if lint and rint:
        print(f'{" "*indent}- comparing ints {a} and {b}')
        if a < b:
            return LESS
        if a == b:
            return EQUAL
        return GREATER
    if not (lint or rint):
        print(f'{" "*indent}- comparing lists {a} and {b}')
        for x, y in itertools.zip_longest(a, b, fillvalue=None):
            #print(f'{" "*indent}- comparing list elements {x} and {y}')
            if x is None:
                return LESS
            if y is None:
                return GREATER
            res = compare(x, y, indent+2)
            if res != EQUAL:
                return res
        return EQUAL
    #print(f'{" "*indent}- comparing {a} ({type(a)}) to {b} ({type(b)})')
    print(f'{" "*indent}- comparing mixed {a} vs {b}')
    if lint:
        return compare([a], b, indent+2)
    return compare(a, [b], indent+2)

index = 0

def proc(a, b):
    global index
    ap, _ = parse(a, 0)
    bp, _ = parse(b, 0)
    res = compare(ap, bp, indent=0)
    index += 1
    print(f'result of pair #{index} {ap} < {bp}: {res}')
    return index, (res == LESS)

def main():
    p = []
    ans = 0
    for line in sys.stdin.readlines():
        line = line.strip()
        if not len(line):
            continue
        print(line)
        p.append(line)
        if len(p) == 2:
            ind, order = proc(p[0], p[1])
            if order:
                ans += ind
            p = []
    if p:
        ind, order = proc(p[0], p[1])
        if order:
            ans += ind
    print(ans)

main()

