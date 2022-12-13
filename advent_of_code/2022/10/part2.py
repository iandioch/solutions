import sys
import collections

def main():
    output_image = [['?' for _ in range(40)] for _ in range(6)]

    def check_cycle(c, val):
        currx = c % 40
        curry = c//40
        if abs(val - currx) > 1:
            output_image[curry][currx] = '.'
        else:
            output_image[curry][currx] = '#'
        print(f'cycle {c} drawn, val {val}, row is {"".join(c for c in output_image[curry] if c != "?")}')

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
        check_cycle(cycle-1, x)
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

    for row in output_image:
        print(''.join(row))

main()
