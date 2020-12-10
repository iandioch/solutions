# k = deck size
# m = minimum draw
# n = maximum draw
# Loser = player who can't make a move
# Finishing with 0 cards left = winning
# Finishing with < m (ie. [0, 1, ..., m-1]) cards left => winning
# Starting with ([m, m+1, ..., m + n - 1]) cards left => winning (as you can
# leave the opponent with < m cards left)
# Finishing with between m and (m+n-1) cards left = losing
# So if k in [0, 1, ...., m-1], (B)arb wins. (max size of list: m - 1) -> B
# If k in [m, m+1, ...., m + n - 1], (A)lex wins. (max size of list: n - 1) -> A
# If k in [m + n, m + n + 1, ..., m + n + m - 1], (B)arb wins? (size of list: m - 1) -> B
# Continue up in these alternating m and n sized lists...?

k, m, n = map(int, input().split())
if k % (m+n) < m:
    print('Barb')
else:
    print('Alex')
