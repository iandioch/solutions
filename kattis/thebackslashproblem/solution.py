import sys


def between(a, b):
    return set(chr(i) for i in range(ord(a), ord(b)+1))

def escape(s):
    out = []
    for c in s:
        if c in special:
            out.append('\\')
        out.append(c)
    return ''.join(out)

special = set()
special = special.union(between('!', '*'))
special = special.union(between('[', ']'))
curr = 0
lines = sys.stdin.readlines()
while curr < len(lines):
    num = int(lines[curr])
    line = lines[curr+1][:-1]
    curr += 2
    for _ in range(num):
        line = escape(line)
    print(line)
