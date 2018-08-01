class Node:
    def __init__(self, num_left, parent):
        self.num_left = num_left
        self.parent = parent

def main():
    n = int(input())
    nodes = list(map(lambda x: Node(x, None), map(int, input().split())))
    for done in range(1, n):
        curr = nodes[done-1]
        while curr is not None and curr.num_left == 0:
            curr = curr.parent
        if curr is None:
            print('NO')
            return
        nodes[done].parent = curr
        curr.num_left -= 1
        nodes[done].num_left -= 1
    ok = all(n.num_left == 0 for n in nodes)
    print('YES' if ok else 'NO')

if __name__ == '__main__':
    main()
