def main():
    import sys
    from math import sqrt
    def dist(a, b, p, q):
        return sqrt((p-a)*(p-a) + (q-b)*(q-b))
    gx, gy, dx, dy = map(float, input().split())

    for line in sys.stdin.readlines():
        sx,sy = line.split()
        x = float(sx)
        y = float(sy)

        gd = dist(gx, gy, x, y)
        dd = dist(dx, dy, x, y)

        #print(f'{x},{y}: gopher = {gd}, dog = {dd}')

        if 2*gd <= dd:
            print(f'The gopher can escape through the hole at ({sx},{sy}).')
            return

    print('The gopher cannot escape.')

main()
