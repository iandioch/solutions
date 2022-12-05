import sys

def main():
    ans = 0
    for line in sys.stdin.readlines():
        a, b = line.strip().split(',')
        i, j = map(int, a.split('-'))
        p, q = map(int, b.split('-'))
        if i == min(i, p) and j == max(j, q):
            # b is contained in a
            ans += 1
        elif p == min(i, p) and q == max(j, q):
            #a is contained in b
            ans += 1
    print(ans)

main()
