import sys
from collections import deque

def get_winning_deck(a, b):
    # left of deque = top of deck
    memo = set()
    while len(a) and len(b):
        at = tuple(a)
        bt = tuple(b)
        if (at, bt) in memo:
            return a, 'A'
        memo.add((at, bt))

        p, q = a.popleft(), b.popleft()
        if len(a) >= p and len(b) >= q:
            ac = deque(card for i, card in enumerate(a) if i < p)
            bc = deque(card for i, card in enumerate(b) if i < q)
            winning_deck, winning_player = get_winning_deck(ac, bc)
            if winning_player == 'A':
                a.append(p)
                a.append(q)
            else:
                b.append(q)
                b.append(p)
        else:
            if p > q:
                a.append(p)
                a.append(q)
            else:
                b.append(q)
                b.append(p)
    return (a, 'A') if len(a) else (b, 'B')

def score_for_deck(a):
    ans = 0
    a.reverse()
    for i, card in enumerate(a):
        mult = i+1
        ans += mult*card
    return ans

def main():
    input() # 'Player 1:'
    a = deque()
    while True:
        line = input()
        if line == '':
            break
        a.append(int(line))

    input() # 'Player 2:'
    b = deque()
    for line in sys.stdin.readlines():
        b.append(int(line))

    winning_deck, winner = get_winning_deck(a, b)
    print(score_for_deck(winning_deck))

main()
