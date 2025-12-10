import heapq
import sys

def solve(target, buttons):
    print(target, buttons)

    q = [(0, [False for _ in range(len(target))])]
    seen = set()
    while True:
        steps, curr = heapq.heappop(q)
        done = True
        for i in range(len(curr)):
            if curr[i] != target[i]:
                done = False
                break
        if done:
            return steps
        ct = tuple(curr[:])
        if ct in seen:
            continue
        seen.add(ct)
        for b in buttons:
            nex = curr[:]
            for bi in b:
                nex[bi] = not nex[bi]
            heapq.heappush(q, (steps + 1, nex))
    return 0

def main():
    ans = 0
    for line in sys.stdin.readlines():
        a, rest = line.split(']')
        target = a[1:]
        target = [c == '#' for c in target]
        print(target)

        buttons, jolts = rest.split('{')
        buttons = buttons[:-1]
        print(buttons)

        blist = []

        for b in buttons.split(')')[:-1]:
            b = b[2:] # remove " ("
            t = list(map(int, b.split(',')))
            blist.append(t)
        ans += solve(target, blist)
    print(ans)

main()
