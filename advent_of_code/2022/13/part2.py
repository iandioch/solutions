import sys
import itertools
import functools

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

LESS = -1
EQUAL = 0
GREATER = 1

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

def proc(a, b):
    ap, _ = parse(a, 0)
    bp, _ = parse(b, 0)
    res = compare(ap, bp, indent=0)
    return res

def main():
    p = [
        '[[2]]',
        '[[6]]'
    ]
    ans = 0
    for line in sys.stdin.readlines():
        line = line.strip()
        if not len(line):
            continue
        print(line)
        p.append(line)
    p.sort(key=functools.cmp_to_key(proc))
    print(p)
    a, b = 0, 0
    for i, x in enumerate(p):
        if a == 0:
            if x == '[[2]]':
                a = i+1
        else:
            if x == '[[6]]':
                b = i+1
    print(a*b)

main()

