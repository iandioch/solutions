from collections import deque

def main():
    n = int(input())
    words = [input() for _ in range(n)]
    word_to_int = {words[i]:i for i in range(n)}
    edges = [[] for _ in range(n)]
    #edges = {w:[] for w in words}

    m = int(input())
    for _ in range(m):
        a, b = input().split()
        i = word_to_int[a]
        j = word_to_int[b]
        edges[i].append(j)
        edges[j].append(i)

    colours = {}
    q = deque()
    qapp = q.append
    for start in range(n):
        if start in colours:
            continue
        qapp((start, True))
        while len(q):
            curr, colour = q.pop()
            if curr in colours and colours[curr] != colour:
                print('impossible')
                return
            colours[curr] = colour
            c = not colour
            for o in edges[curr]:
                if o in colours:
                    if colours[o] != c:
                        print('impossible')
                        return
                else:
                    qapp((o, c))
    ans = [[], []]
    for k in colours:
        ans[int(colours[k])].append(words[k])
    print(*ans[0])
    print(*ans[1])


if __name__ == '__main__':
    main()
