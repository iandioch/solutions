def main():
    target = int(input())
    bus = [None if c == 'x' else int(c) for c in input().split(',')]
    active_bus = [b for b in bus if b is not None]

    t = target
    while True:
        for b in active_bus:
            if t % b == 0:
                print((t - target)*b)
                return
        t += 1

main()
