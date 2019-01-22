def main():
    ncountry, nborder = map(int, input().split())
    adj = [[] for _ in range(ncountry)]
    for _ in range(nborder):
        i, j = map(int, input().split())
        adj[i].append(j)
        adj[j].append(i)
    colours = [-1 for _ in range(ncountry)]
    colours[0] = 0
    ok = False
    for ncol in range(1, 5):
        colset = set(range(ncol))
        def try_combo():
            curr = next((a for a in range(ncountry) if colours[a] == -1), -1)
            if curr == -1:
                # all are coloured
                ok = True
                print(ncol)
                return True
            poss = colset - set(colours[i] for i in adj[curr] if colours[i] != -1)
            if len(poss) == 0:
                ok = False
                return False
            for col in poss:
                colours[curr] = col
                if try_combo():
                    return True
                else:
                    colours[curr] = -1


        ok = try_combo()
        if ok:
            break


    if not ok:
        print('many')

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        main()
