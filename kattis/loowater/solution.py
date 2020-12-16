def main():
    while True:
        num_heads, num_knights = map(int, input().split())
        if num_heads == num_knights == 0:
            return
        heads = list(sorted(map(int, (input() for _ in range(num_heads)))))
        knights = list(sorted(map(int, (input() for _ in range(num_knights)))))
        h = 0
        k = 0

        tot = 0
        while True:
            if h >= len(heads):
                break
            if k >= len(knights):
                break

            if heads[h] > knights[k]:
                k += 1
                continue

            tot += knights[k]
            h += 1
            k += 1
        if h >= len(heads):
            print(tot)
        else:
            print('Loowater is doomed!')

main()
