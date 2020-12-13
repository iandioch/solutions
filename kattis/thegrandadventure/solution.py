from collections import deque

def do_adventure(s):
    bag = deque()
    d = {'b': '$', 'j': '*', 't': '|'}
    for c in s:
        if c in '$|*':
            bag.append(c)
        elif c in 'tjb':
            item = None
            while item != d[c]:
                if not len(bag):
                    return False
                item = bag.pop()
    return len(bag) == 0


n = int(input())
for _ in range(n):
    if do_adventure(input()):
        print('YES')
    else:
        print('NO')
