import sys

def get_overlapping_range(a, b):
    if a[0] >= b[0] and a[0] <= b[1]:
        a, b = b, a
    if b[0] >= a[0] and b[0] <= a[1]:
        return a[0], max(a[1], b[1])
    return None


def main():
    p = []
    g = []
    for line in sys.stdin.readlines():
        line = line.strip()
        if not len(line):
            continue
        if '-' in line:
            a, b = line.split('-')
            p.append((int(a), int(b)))
        else:
            g.append(int(line))

    # Merge ranges
    while True:
        found = False

        for i in range(len(p)-1):
            for j in range(i+1, len(p)):
                overlap = get_overlapping_range(p[i], p[j])
                if overlap is not None:
                    new_p = []
                    for x in range(len(p)):
                        if x != i and x != j:
                            new_p.append(p[x])
                    new_p.append(overlap)
                    p = new_p
                    found = True
                    break
            if found:
                break
        if not found:
            break

    ans = 0
    for f in p:
        ans += f[1] - f[0] + 1
    print(ans)



main()
