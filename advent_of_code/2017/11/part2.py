class CubeHex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dist_to_hex(self, other):
        return self.dist_to_coord(other.x, other.y, other.z)

    def dist_to_coord(self, i, j, k):
        return (abs(self.x - i) + abs(self.y - j) + abs(self.z - k))//2

    def neighbours(self):
        return {
            'n': CubeHex(self.x, self.y + 1, self.z - 1),
            'ne': CubeHex(self.x + 1, self.y, self.z - 1),
            'se': CubeHex(self.x + 1, self.y - 1, self.z),
            's': CubeHex(self.x, self.y - 1, self.z + 1),
            'sw': CubeHex(self.x - 1, self.y, self.z + 1),
            'nw': CubeHex(self.x - 1, self.y + 1, self.z),
        }
        
path = input().split(',')
start = CubeHex(0, 0, 0)
curr = CubeHex(0, 0, 0)
ans = 0
for step in path:
    curr = curr.neighbours()[step]
    ans = max(ans, curr.dist_to_hex(start))

print(ans)
