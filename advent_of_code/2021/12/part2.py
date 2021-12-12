import sys
from collections import defaultdict, deque

def can_move(path, other, is_small):
    if other == 'start':
        return False
    if not is_small[other]:
        return True
    if other not in path:
        return True

    d = defaultdict(int)
    for p in path:
        if not is_small[p]:
            continue
        d[p] += 1
    for e in d:
        if d[e] > 1:
            return False
    return True

def count_paths(d, is_small):
    q = deque()
    q.append(('start', ['start']))

    finish = set()
    while len(q):
        pos, path = q.popleft()
        if pos == 'end':
            finish.add('-'.join(path))
            continue
        for other in d[pos]:
            if can_move(path, other, is_small):
                q.append((other, path[:] + [other]))
    return len(finish)

def main():
    d = defaultdict(list)
    for line in sys.stdin.readlines():
        a, b = line.strip().split('-')
        d[a].append(b)
        d[b].append(a)
    is_small = {c:(c.lower() == c) for c in d}
    print(count_paths(d, is_small))

main()
