class LinkedListNode:
    def __init__(self, d):
        self.d = d
        self.nex = None

    def add_to_end(self, node):
        n = self
        while n.nex is not None:
            n = n.nex
        n.nex = node

    def __str__(self):
        a = []
        n = self
        while n is not None:
            a.append(n.d)
            n = n.nex
        return '[' + ', '.join(map(str, a)) + ']'

def base_prob(a, b):
    ans = LinkedListNode(0)
    overflow = 0
    while True:
        if a is None and b is None:
            break
        x = overflow
        if a is not None:
            x += a.d
            a = a.nex
        if b is not None:
            x += b.d
            b = b.nex
        if x > 10:
            x -= 10
            overflow = 1
        ans.add_to_end(LinkedListNode(x))
    return ans.nex

def followup_prob(a, b):
    def r(x, y):
        a = x.d + y.d
        m = None
        if x.nex is not None:
            o, m = r(x.nex, y.nex)
            a += o
        l = LinkedListNode(a%10)
        l.nex = m
        return a > 10, l
    xl = 0
    yl = 0
    p = a
    while p is not None:
        p = p.nex
        xl += 1
    p = b
    while p is not None:
        p = p.nex
        yl += 1
    for _ in range(xl, yl, 1):
        # xl < yl
        l = LinkedListNode(0)
        l.nex = a
        a = l
    for _ in range(yl, xl, 1):
        # xl < yl
        l = LinkedListNode(0)
        l.nex = b
        b = l
    o, ans = r(a, b)
    if o > 0:
        l = LinkedListNode(1)
        l.nex = ans
        return l
    return ans


if __name__ == '__main__':
    a = LinkedListNode(7)
    a.add_to_end(LinkedListNode(1))
    a.add_to_end(LinkedListNode(6))

    b = LinkedListNode(5)
    b.add_to_end(LinkedListNode(9))
    b.add_to_end(LinkedListNode(2))
    print(str(base_prob(a, b)))

    a = LinkedListNode(6)
    a.add_to_end(LinkedListNode(1))
    a.add_to_end(LinkedListNode(7))

    b = LinkedListNode(2)
    b.add_to_end(LinkedListNode(9))
    b.add_to_end(LinkedListNode(5))
    print(str(followup_prob(a, b)))

