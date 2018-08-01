from collections import deque

class Node:
    def __init__(self, num):
        self.num = num
        self.edges = [] # nodes 
        self.left = False
        self.left_edges = set() # set of ID integers

def main():
    num_countries, num_partnerships, home, first = map(int, input().split())
    countries = [Node(i) for i in range(num_countries)]
    first -= 1
    home -= 1
    if first == home:
        print('leave')
        return

    for _ in range(num_partnerships):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        countries[a].edges.append(countries[b])
        countries[b].edges.append(countries[a])

    q = deque()
    for o in countries[first].edges:
        o.left_edges.add(first)
        q.append(o)
    while len(q):
        curr = q.popleft()
        if curr.left:
            continue
        if len(curr.left_edges)*2 >= len(curr.edges):
            # curr = leaving
            curr.left = True
            if curr.num == home:
                print('leave')
                return
            for o in curr.edges:
                if o.left:
                    continue
                o.left_edges.add(curr.num)
                q.append(o)
    print('stay')

if __name__ == '__main__':
    main()
