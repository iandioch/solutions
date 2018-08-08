import sys
sys.setrecursionlimit(1500)

class Endpoint:
    def __init__(self, curr):
        self.parent = self
        self.curr = curr

    def union(self, other):
        aroot = self.find()
        broot = other.find()
        aroot.parent = broot

    def find(self):
        if self.parent.curr != self.curr:
            self.parent = self.parent.find()
        return self.parent

def main():
    ncity = int(input())
    for _ in range(ncity):
        n = int(input())
        c = [Endpoint(i) for i in range(n)]
        for _ in range(int(input())):
            a, b = map(int, input().split())
            c[a].union(c[b])

        g = set()
        for d in c:
            p = d.find()
            g.add(p.curr)
        print(len(g)-1)
 
if __name__ == '__main__':
    main()
