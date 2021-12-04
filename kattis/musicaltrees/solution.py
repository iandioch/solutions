def main():
    num_people, num_tree = map(int, input().split())
    people = list(map(int, input().split()))
    tree = sorted(list(map(int, input().split())))

    best_tree = [-1 for _ in people]
    for j, p in enumerate(people):
        best = 0
        dif = abs(tree[0] - p)
        for i, t in enumerate(tree):
            d = abs(t - p)
            if d < dif:
                dif = d
                best = i

        best_tree[j] = best
    print(num_people - len(set(best_tree)))

main()

