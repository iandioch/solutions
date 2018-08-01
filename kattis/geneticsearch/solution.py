import sys

def count_with_overlaps(s, seek):
    i = 0
    ans = 0
    while True:
        i = s.find(seek, i) + 1
        if i > 0:
            ans += 1
        else:
            return ans
            

def op(a, b):
    i = count_with_overlaps(b, a)

    j = 0
    deleted = set()
    for p in range(len(a)):
        c = a[:p] + a[p+1:]
        if c in deleted:
            continue
        deleted.add(c)
        j += count_with_overlaps(b, c)

    k = 0
    added = set()
    for p in range(len(a) + 1):
        for c in 'AGCT':
            s = a[:p] + c + a[p:]
            added.add(s)
    for s in added:
        k += count_with_overlaps(b, s)

    return i, j, k 

def main():
    for line in sys.stdin:
        s = line.split()
        if s[0] == '0':
            break
        print(*op(s[0], s[1]))

if __name__ == '__main__':
    main()
