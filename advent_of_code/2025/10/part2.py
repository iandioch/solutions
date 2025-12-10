import heapq
import sys

from collections import defaultdict

MAX_INT = 1 << 32

def solve_n(orig_target, orig_buttons):
    best_so_far = MAX_INT

    buttons = [] # sorted(orig_buttons, key=lambda x:-len(x))
    while len(orig_buttons):
        d = defaultdict(int)
        for b in orig_buttons:
            for i in b:
                d[i] += 1
        # Which light has the fewest buttons that toggle it?
        minn = min(d, key=lambda x:d[x])

        minn = None
        for i in range(len(orig_target)):
            if d[i] == 0:
                continue
            if minn is None:
                minn = i
                continue
            if d[i] < d[minn] or (d[i] == d[minn] and orig_target[i] > orig_target[minn]):
                minn = i


        # Which button that toggles the most fussy light has the most other
        # effects?
        next_button = None
        for i in range(len(orig_buttons)):
            if minn in orig_buttons[i]:
                if next_button is None:
                    next_button = i
                elif len(orig_buttons[next_button]) < len(orig_buttons[i]):
                    next_button = i
        buttons.append(orig_buttons[next_button])
        del orig_buttons[next_button]

    is_last_button = {}
    for i in range(len(buttons)):
        bset = set(buttons[i])
        for j in range(i+1, len(buttons)):
            bset -= set(buttons[j])
        is_last_button[i] = bset

    print(is_last_button)

    def _solve(target, curr_button, steps_so_far):
        nonlocal best_so_far
        if steps_so_far >= best_so_far:
            return

        if curr_button == len(buttons):
            if all(t == 0 for t in target):
                best_so_far = min(best_so_far, steps_so_far)
                print(orig_target, best_so_far)
            return

        min_press = 0
        for i in is_last_button[curr_button]:
            min_press = max(min_press, target[i])

        max_press = min(target[i] for i in buttons[curr_button])
        if max_press < min_press:
            return

        for i in range(min_press, max_press+1):
            new_target = target[:]
            for j in buttons[curr_button]:
                new_target[j] -= i
            _solve(new_target, curr_button+1, steps_so_far + i)

    _solve(orig_target, 0, 0)
    return best_so_far

def main():
    ans = 0
    for line in sys.stdin.readlines():
        a, rest = line.split(']')
        target = a[1:]
        target = [c == '#' for c in target]

        buttons, jolts = rest.split('{')
        buttons = buttons[:-1]

        jolts = jolts[:-2] # remove "}\n"
        jolts = list(map(int, jolts.split(',')))

        blist = []

        for b in buttons.split(')')[:-1]:
            b = b[2:] # remove " ("
            t = list(map(int, b.split(',')))
            blist.append(t)

        sol = solve_n(jolts, blist)
        print("sol", sol)
        ans += sol
    print('Final answer:', ans)

main()
