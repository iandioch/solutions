from sys import stdin

def main():
    rl = stdin.readline
    d = {}
    n = int(rl())
    for _ in range(n):
        word = rl().strip()
        e = d
        for c in word:
            if c in e:
                e[c][0] += 1
            else:
                e[c] = [0, {}]
            ans = e[c][0]
            e = e[c][1]
        print(ans)

main()
