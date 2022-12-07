class File:
    def __init__(self, name, size):
        self._name = name
        self._size = size

    def size(self):
        return self._size

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = {}

    def size(self):
        return sum(self.contents[c].size() for c in self.contents)

import sys

def main():
    root = Dir('/', None)
    currdir = root
    inputs = [line.strip() for line in sys.stdin.readlines()]

    pi = 0
    while pi < len(inputs):
        p = inputs[pi].split()
        if p[0] != '$':
            print('Error: not a command', inputs[pi])
            return

        if p[1] == 'ls':
            if len(currdir.contents):
                print('Error: repeated ls')
                return

            j = pi + 1
            while j < len(inputs):
                if inputs[j][0] == '$':
                    break
                q = inputs[j].split()
                if q[0] == 'dir':
                    d = Dir(q[1], currdir)
                    currdir.contents[q[1]] = d
                else:
                    f = File(q[1], int(q[0]))
                    currdir.contents[q[1]] = f
                j += 1
            pi = j
            continue
        # cd
        if p[2] == '/':
            currdir = root
            pi += 1
            continue
        if p[2] == '..':
            currdir = currdir.parent
            pi += 1
            continue
        currdir = currdir.contents[p[2]]
        pi += 1

    import collections
    q = collections.deque()
    q.append(root)
    best = root
    bestsize = root.size()
    MAX = 70000000
    REQ = 30000000
    USED = bestsize
    while len(q):
        d = q.popleft()
        size = d.size()
        if (MAX - USED + size >= REQ) and size < bestsize:
            print(d.name, size)
            best = d
            bestsize = size
        for e in d.contents.values():
            if isinstance(e, Dir):
                q.append(e)
    print(bestsize)


main()
