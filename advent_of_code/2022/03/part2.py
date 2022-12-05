import sys

def get_prio(c):
    co = ord(c)
    if co <= ord('Z'):
        # uppercase
        return co - ord('A') + 27
    return co - ord('a') + 1

def handle_pack(line):
    a, b = line[:len(line)//2], line[len(line)//2:]
    return get_prio(next(iter(set(a) & set(b))))

def handle_trio(d):
    badge = (next(iter(set(d[0]) & set(d[1]) & set(d[2]))))
    print(d, badge)
    return get_prio(badge)

def main():
    tot = 0
    d = []
    for line in sys.stdin.readlines():
        d.append(line.strip())
        if len(d) == 3:
            p = handle_trio(d)
            d = []
            tot += p
    print(tot)

main()
