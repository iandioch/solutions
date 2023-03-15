import sys

NEEDS_PRE = False

def proc(words):
    global NEEDS_PRE
    if not len(words):
        return
    if NEEDS_PRE:
        print()
    NEEDS_PRE = True
    longest = max(len(w) for w in words)
    so = sorted(words, key=lambda w:w[::-1])
    for s in so:
        print(' '*(longest-len(s)) + s)

def main():
    lines = [l.strip() for l in sys.stdin.readlines()]
    ip = -1
    words = []
    while ip < len(lines)-1:
        ip += 1
        if not len(lines[ip]):
            proc(words)
            words = []
        else:
            words.append(lines[ip])
    proc(words)


main()
