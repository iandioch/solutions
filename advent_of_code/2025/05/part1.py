import sys

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

    ans = 0
    for ingredient in g:
        for fresh in p:
            if ingredient >= fresh[0] and ingredient <= fresh[1]:
                ans += 1
                break
    print(ans)

main()
