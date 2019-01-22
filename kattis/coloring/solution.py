def main():
    num_vert = int(input())
    adj = [None]*num_vert
    for i in range(num_vert):
        adj[i] = list(map(int, input().split()))
    num_col = 1
    while True:
        num_col += 1

        def try_combo(colours):
            curr = next((c for c in range(num_vert) if colours[c] == -1), -1)
            if curr == -1:
                return True
            poss = set(range(num_col)) - set(colours[i] for i in adj[curr] if colours[i] != -1)
            for col in poss:
                colours[curr] = col
                if try_combo(colours):
                    return True
                colours[curr] = -1
            return False
        combo = [-1 for _ in range(num_vert)]
        combo[0] = 0
        combo[adj[0][0]] = 1
        if try_combo(combo):
            break
    print(num_col)

if __name__ == '__main__':
    main()
