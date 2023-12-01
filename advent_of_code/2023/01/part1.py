import sys

def main():
    DIGITS = {c: int(c) for c in '0123456789'}
    tot = 0
    for line in sys.stdin.readlines():
        da, db = 0, 0
        for a in line:
            if a in DIGITS:
                da = DIGITS[a]
                break
        for b in line[::-1]:
            if b in DIGITS:
                db = DIGITS[b]
                break
        tot += da*10 + db
    print(tot)


if __name__ == '__main__':
    main()
