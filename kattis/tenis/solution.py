P, Q = input().split()
n = int(input())


'''
Returns (ok, winner), where:
ok = whether or not it was a valid set
winner = the index of the winning player
'''
def analyse_set(a, b, set_num, p, q):
    if a == b:
        return False, 0
    winner = 0
    if a < b:
        # Swap for handiness' sake, so a has higher score.
        winner = 1
        a, b = b, a
        p, q = q, p
    if q == 'federer':
        # Federer must win
        return False, winner
    if a < 6:
        # Winner needs to have at least 6 games won.
        return False, winner
    if a == 6:
        # Must have at least 2 more games than their opponent.
        return b <= 4, winner
    if a == 7 and set_num < 2:
        return (b in (5, 6)), winner
    if a >= 7 and set_num == 2:
        return a == b+2, winner
    return False, winner


for _ in range(n):
    sets = input().split()
    ok = True
    win = [0, 0]
    for i in range(len(sets)):
        s = sets[i]
        a, b = map(int, s.split(':'))

        # Make sure there's no extra set after someone already won
        ok &= win[0] < 2
        ok &= win[1] < 2

        o, winner = analyse_set(a, b, i, P, Q)

        win[winner] += 1
        ok &= o

    # Make sure someone won
    if ok and (win[0] == 2 or win[1] == 2):
        print('da')
    else:
        print('ne')
