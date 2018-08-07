def main():
    h, w, r = map(int, input().split())
    lines = [input() for _ in range(h)]
    best = 0
    best_c = (0, 0)
    for i in range(0, w-r + 1):
        for j in range(0, h-r + 1):
            tot = 0
            for x in range(i + 1, i + r - 1):
                for y in range(j + 1, j + r - 1):
                    if lines[y][x] == '*':
                        tot += 1
            if tot > best:
                best_c = (i, j)
                best = tot
    print(best)

    x, y = best_c
    for j in range(0, h):
        if j < y or j >= y + r:
            print(lines[j])
            continue
        out = []
        for i in range(0, w):
            inside = (i >= x and i < x + r)
            if not inside:
                out.append(lines[j][i])
                continue
            corner = ((i == x and j == y) or
                      (i == (x+r-1) and j == y) or
                      (i == x and j == (y+r-1)) or
                      (i == (x+r-1) and j == (y+r-1)))
            if corner:
                out.append('+')
                continue
            if i == x or i == (x + r - 1):
                out.append('|')
            elif j == y or j == (y + r - 1):
                out.append('-')
            else:
                out.append(lines[j][i])
        print(''.join(out))

if __name__ == '__main__':
    main()
