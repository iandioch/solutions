import sys

def visualise(hj, tj):
    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    for x, y in hj+tj:
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)

    for i in range(len(hj)):
        for y in range(miny, maxy+1):
            line = []
            for x in range(minx, maxx+1):
                if (x, y) == hj[i]:
                    line.append('H')
                elif (x, y) == tj[i]:
                    line.append('T')
                elif (x, y) == (0, 0):
                    line.append('s')
                else:
                    line.append('.')
            print(''.join(line))
        print('')


def calc(moves):
    hx, hy = (0, 0)
    tx, ty = (0, 0)

    def must_move():
        return not ((abs(hx-tx) <= 1) and (abs(hy-ty) <= 1))


    tj = []
    hj = []
    for i, j in moves:
        hx += i
        hy += j

        if must_move():
            if hx == tx:
                # same column
                ty += 1 if (hy > ty) else -1
            elif hy == ty:
                # same row
                tx += 1 if (hx > tx) else -1
            else:
                # diag
                bestp = None
                bestd = 100000
                for p in [(tx-1, ty-1), (tx+1, ty-1), (tx-1, ty+1), (tx+1, ty+1)]:
                    d = (hx-p[0])**2 + (hy-p[1])**2
                    if d < bestd:
                        bestd = d
                        bestp = p

                (tx, ty) = bestp
        hj.append((hx, hy))
        tj.append((tx, ty))

    #visualise(hj, tj)

    return len(set(tj))

def main():
    moves = []
    for line in sys.stdin.readlines():
        d, n = line.strip().split()
        n = int(n)
        for _ in range(n):
            if d == 'U':
                moves.append((0, -1))
            elif d == 'R':
                moves.append((1, 0))
            elif d == 'L':
                moves.append((-1, 0))
            elif d == 'D':
                moves.append((0, 1))
            else:
                print('error', d)

    print(calc(moves))

main()
