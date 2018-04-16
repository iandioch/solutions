n, m = map(int, input().split())
num_probs = {i:0 for i in range(1, n+1)}
penalty = {i:0 for i in range(1, n+1)}
better = set()

for _ in range(m):
    team, p = map(int, input().split())

    pn = num_probs[team]
    pp = penalty[team]

    num_probs[team] += 1
    penalty[team] += p

    nn = num_probs[team]
    np = penalty[team]

    if team == 1:
        for other in list(better):
            if num_probs[other] < nn:
                better.remove(other)
            elif num_probs[other] == nn and penalty[other] >= np:
                better.remove(other)
        print(len(better) + 1)
        continue


    if nn == num_probs[1] + 1:
        better.add(team)
    if nn == num_probs[1] and np < penalty[1]:
        better.add(team)
    print(len(better)+1)
