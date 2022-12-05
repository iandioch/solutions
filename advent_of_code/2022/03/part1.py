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

def main():
    tot = 0
    for line in sys.stdin.readlines():
        p = handle_pack(line)
        tot += p
    print(tot)

main()
