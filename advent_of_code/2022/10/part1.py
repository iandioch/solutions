import sys
import collections

def main():
    ans = 0
    def interesting_cycle(c):
        if c == 20:
            return True
        return (c-20)%40 == 0

    def check_cycle(c, val):
        nonlocal ans 
        if not interesting_cycle(c):
            return
        print(c, val, c*val)
        ans += c*val

    x = 1
    cycle = 0
    xd = collections.deque()

    def proc_cycle():
        nonlocal x
        nonlocal cycle
        while len(xd):
            if xd[0][0] == cycle:
                c, d = xd.popleft()
                x += d
            else:
                break
        check_cycle(cycle, x)
        cycle += 1

    for line in sys.stdin.readlines():
        p = line.strip().split()
        proc_cycle()
        if len(p) == 1:
            # noop
            pass
        else:
            v = int(p[1])
            xd.append((cycle+2, v))
            proc_cycle()

    while len(xd):
        proc_cycle()
        cycle += 1

    print(x, ans)


main()
