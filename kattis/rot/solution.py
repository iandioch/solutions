def print_skewed(g):
    i = 0

    numspace = len(g) - 1
    ch = -1
    while True:
        t = 0
        out = []
        for y in range(len(g)):
            x = i-y
            if x < 0 or x >= len(g[y]):
                continue
            t += 1
            out.append(g[y][x])
        print(' '*numspace + ' '.join(out[::-1]))
        numspace += ch
        if numspace == 0:
            ch *= -1
        i += 1
        if t == 0:
            break

def rotate(g):
    return list(zip(*g[::-1]))

def main():
    h, w = map(int, input().split())
    g = [[c for c in input().strip()] for line in range(h)]
    angle = int(input())

    angle %= 360

    while angle >= 90:
        g = rotate(g)
        angle -= 90

    if angle == 45:
        print_skewed(g)
    else:
        for h in g:
            print(''.join(h))

if __name__ == '__main__':
    main()
