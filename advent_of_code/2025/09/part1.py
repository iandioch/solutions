import sys

def area(a, b, x, y):
    return (1+abs(a-x))*(1+abs(b-y))

def main():
    g = []
    ans = 0
    for line in sys.stdin.readlines():
        a, b = map(int, line.strip().split(','))
        for x, y in g:
            ans = max(ans, area(a, b, x, y))
        g.append((a, b))

    print(ans)

main()
