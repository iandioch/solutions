class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, v):
        if self.val is None:
            self.val = v
            return ''
        if v < self.val:
            if self.left is None:
                self.left = Node(v)
                return
            self.left.insert(v)
        else:
            if self.right is None:
                self.right = Node(v)
                return
            self.right.insert(v)

    def iter(self):
        if not self.left and not self.right:
            return '$'
        ans = ''
        if self.left:
            ans += 'L'
            ans += self.left.iter()
        if self.right:
            ans += 'R'
            ans += self.right.iter()
        return ans + '$'

num_protos, num_layers = map(int, input().split())
ans = set()
for _ in range(num_protos):
    p = map(int, input().split())
    root = Node(None)
    for q in p:
        root.insert(q)
    ans.add(root.iter())
print(len(ans))
