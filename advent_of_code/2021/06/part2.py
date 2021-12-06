def main():
    PRINT = False

    nums = list(map(int, input().split(',')))

    num_days = 256
    g = [0 for _ in range(10)]
    for n in nums:
        g[n] += 1

    for d in range(num_days):
        new_g = [0 for _ in range(len(g))]
        for i in range(1, len(g)):
            new_g[i-1] = g[i]

        new_g[6] += g[0]
        new_g[8] += g[0]

        g = new_g

    print(sum(g))

main()

