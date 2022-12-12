import sys

def visualise(history):
    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    for segment in history:
        for x, y in segment:
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)

    for i in range(len(history[0])):
        for y in range(miny, maxy+1):
            line = []
            for x in range(minx, maxx+1):
                is_rope = False
                for segment in range(len(history)):
                    if (x, y) == history[segment][i]:
                        if segment == 0:
                            line.append('H')
                        else:
                            line.append(str(segment))
                        is_rope = True
                        break
                if is_rope:
                    continue
                if (x, y) == (0, 0):
                    line.append('s')
                else:
                    line.append('.')
            print(''.join(line))
        print('')


def calc(moves):
    rope = []
    history = []
    for _ in range(10):
        rope.append((0, 0))
        history.append([])

    def must_move(hx, hy, tx, ty):
        return not ((abs(hx-tx) <= 1) and (abs(hy-ty) <= 1))


    for i, j in moves:
        rope[0] = (rope[0][0] + i, rope[0][1] + j)
        print('curr:', rope[0])
        for segment in range(1, len(rope)):
            hx, hy = rope[segment-1]
            tx, ty = rope[segment]
            print(f'segment {segment} @ {tx, ty}, with head {hx, hy}, must move: {must_move(hx, hy, tx, ty)}.')

            if must_move(hx, hy, tx, ty):
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
                        d = abs(hx-p[0]) + abs(hy-p[1])
                        if d < bestd:
                            bestd = d
                            bestp = p
                    (tx, ty) = bestp

                if (tx, ty) != rope[segment]:
                    print(f'moving segment {segment} to {tx, ty}.')
                rope[segment] = (tx, ty)
        for segment in range(len(rope)):
            print(segment, rope[segment])
            history[segment].append(rope[segment])

    #visualise(history)
    return len(set(history[-1]))

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
