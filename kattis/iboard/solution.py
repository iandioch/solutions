import sys

def trapped(s):
    one, zero = True, True # ok to leave
    for c in s:
        b = bin(ord(c))[2:].zfill(7)
        for v in b[::-1]:
            if v == '1':
                one = not one
            else:
                zero = not zero
    return 'free' if (zero and one) else 'trapped'

for line in sys.stdin.readlines():
    line = line[:-1]
    print(trapped(line))
