import sys
import heapq

def solve(task, shapes):
    #shapes = shapes[::-1]
    print(f'Solving task {task} for {len(shapes)} shapes: {shapes}')
    rots = [[] for shape in shapes]
    req_per_shape = []
    for shape in shapes:
        r = 0
        for row in shape:
            r += sum(1 for c in row if c)
        req_per_shape.append(r)

    def g_equal(a, b):
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] != b[i][j]:
                    return False
        return True

    for shape_index in range(len(shapes)):
        rots[shape_index].append(shapes[shape_index])
        #print('Root shape')
        #print('\n'.join([''.join(['#' if c else '.' for c in row]) for row in rots[shape_index][-1]]))
        for i in range(3):
            # Rot the previous one 90deg
            s = rots[shape_index][-1]
            t = [[False for _ in range(3)] for _ in range(3)]
            for pos, row_ind in enumerate(range(2, -1, -1)):#2, -1, -1):
                for col_ind in range(3):
                    t[col_ind][pos] = s[row_ind][col_ind]
            if not any(g_equal(r, t) for r in rots[shape_index]):
                rots[shape_index].append(t)

        # Put in horizontal mirrors
        for s in rots[shape_index][:]:
            t = []
            for x in range(2, -1, -1):
                row = []
                for y in range(3):
                    row.append(s[x][y])
                t.append(row)
            if not any(g_equal(r, t) for r in rots[shape_index]):
                rots[shape_index].append(t)

        # Put in vertical mirrors
        for s in rots[shape_index][:]:
            t = []
            for x in range(3):
                row = []
                for y in range(2, -1, -1):
                    row.append(s[x][y])
                t.append(row)
            if not any(g_equal(r, t) for r in rots[shape_index]):
                rots[shape_index].append(t)

    def _place(g, shape_index, rot=0):
        #print(f'Trying to place shape {shape_index} rot {rot} in {g}')
        for x in range(len(g)-2):
            for y in range(len(g[0])-2):
                #print(f'Testing {x} {y} of {len(g)-3}, {len(g[0])-3}')
                fits = True
                for i in range(3):
                    if not fits:
                        break
                    for j in range(3):
                        needed = rots[shape_index][rot][i][j]
                        if not needed:
                            continue
                        if needed and g[x+i][y+j]:
                            fits = False
                            #print(f"Can't place at {x}, {y} because of {x+i}{y+j}")
                            break
                if fits:
                    #print(f'Shape {shape_index} rot {rot} fits at {x}, {y}')
                    wasted = 0
                    placed = 0
                    g_copy = [row[:] for row in g]
                    for i in range(3):
                        for j in range(3):
                            needed = rots[shape_index][rot][i][j]
                            if needed:
                                g_copy[x+i][y+j] = True
                                placed += 1
                            elif not g_copy[x+i][y+j]:
                                wasted += 1
                    return g_copy, wasted, placed
        return None


    def _solve(orig_g, orig_req):
        q = [(sum(orig_req), 0, 0, orig_g, orig_req)]

        it = 0
        while len(q):
            n, wasted, num_placed, g, req = heapq.heappop(q)
            if it % 1000 == 0:
                print(n, wasted, req, len(q))
                for row in g:
                    print(''.join('#' if c else '.' for c in row))
            it += 1
            if n == 0:
                return True
            req_left = sum(req[i] * req_per_shape[i] for i in range(len(req)))
            if req_left + wasted + num_placed > len(g)*len(g[0]):
                continue
            for shape_index in range(len(req)):
                if req[shape_index] > 0:
                    for rot in range(len(rots[shape_index])):
                        placed = _place(g, shape_index, rot)
                        if placed is None:
                            continue
                        new_g, w, p = placed
                        req_copy = req[:]
                        req_copy[shape_index] -= 1
                        heapq.heappush(q, (n - 1, wasted + w, num_placed + p, new_g, req_copy))
        return False



    w, h = task[0]
    req = task[1]
    g = [[False for _ in range(h)] for _ in range(w)]
    return _solve(g, req)

def main():
    tasks = []
    shapes = []

    in_shape = False
    for line in sys.stdin.readlines():
        line = line.strip()
        if not len(line):
            in_shape = False
            continue
        if 'x' in line:
            bounds, quant = line.split(':')
            bounds = tuple(map(int, bounds.strip().split('x')))
            quants = list(map(int, quant.strip().split(' ')))
            tasks.append((bounds, quants))
        elif ':' in line:
            in_shape = True
            shapes.append([])
        else:
            shapes[-1].append([c == '#' for c in line.strip()])

    print(shapes)
    print(tasks)
    ans = 0
    for i, t in enumerate(tasks):
        (w, h), req = t
        req_per_shape = []
        for shape in shapes:
            r = 0
            for row in shape:
                r += sum(1 for c in row if c)
            req_per_shape.append(r)
        print(req_per_shape)
        min_space = sum(req[i]*req_per_shape[i] for i in range(len(t)))
        if min_space > (w*h):
            print(f'Task {t} impossible to solve, skipping')
            continue
        elif sum(req) <= (w//3)*(h//3):
            print(f'Task {t} trivially solveable, skipping')
            ans += 1
            continue
        print('Unsure')
        sol = solve(t, shapes)
        print(f'Task {t} solveable? {sol}')
        if sol:
            ans += 1
    print(ans)


main()
