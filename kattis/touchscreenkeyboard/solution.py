def proc(pos):
    s, n = input().split()
    n = int(n)
    a = []
    for _ in range(n):
        t = input()
        d = sum(abs(pos[a][0] - pos[b][0]) + abs(pos[a][1] - pos[b][1]) for a, b in zip(s, t))
        a.append((d, t))
    print('\n'.join('{} {}'.format(b[1], b[0]) for b in sorted(a)))

def main():
    s = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    pos = {}
    for i in range(3):
        for j in range(len(s[i])):
            c = s[i][j]
            pos[c] = (i, j)
    num = int(input())
    for _ in range(num):
        proc(pos)

if __name__ == '__main__':
    main()
