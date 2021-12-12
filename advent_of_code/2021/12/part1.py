import sys
from collections import defaultdict, deque

def count_paths(d, is_small):
    q = deque()
    q.append(('start', []))

    finish = set()
    while len(q):
        pos, path = q.popleft()
        if pos == 'end':
            finish.add('-'.join(path))
            continue
        for other in d[pos]:
            if is_small[other] and other in path:
                continue
            q.append((other, path + [pos]))
    print('\n'.join(sorted(finish)))
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
