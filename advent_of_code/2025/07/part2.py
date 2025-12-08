import sys

def main():
    n = set()
    ans = 0

    for line in sys.stdin.readlines():
        c = line.strip()
        new_n = set()
        for i in range(len(c)):
            if c[i] == 'S':
                new_n.add(i)
                break
            elif c[i] == '.':
                if i in n:
                    new_n.add(i)
            elif c[i] == '^':
                if i in n:
                    ans += 1
                    if i > 0:
                        new_n.add(i-1)
                    if i < len(c) - 1:
                        new_n.add(i+1)
        n = new_n
    print(ans)

main()

