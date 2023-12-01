import sys

def substr_from(s, i, search):
    if i + len(search) > len(s):
        return False
    return s[i:i+len(search)] == search

DIGITS = {c: int(c) for c in '0123456789'}
def get_dig(s, i):
    if s[i] in DIGITS:
        return DIGITS[s[i]]
    for n, num in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        if substr_from(s, i, num):
            return n+1
    return None


def main():
    tot = 0
    for line in sys.stdin.readlines():
        line = line.strip()
        da, db = 0, 0
        for i in range(len(line)):
            x = get_dig(line, i)
            if x is not None:
                da = x
                break
        for i in range(len(line)-1, -1, -1):
            x = get_dig(line, i)
            if x is not None:
                db = x
                break
        tot += da*10 + db
    print(tot)


if __name__ == '__main__':
    main()
