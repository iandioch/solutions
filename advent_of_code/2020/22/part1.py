import sys
from collections import deque

def get_winning_deck(a, b):
    # left of deque = top of deck
    while len(a) and len(b):
        p, q = a.popleft(), b.popleft()
        if p > q:
            a.append(p)
            a.append(q)
        else:
            b.append(q)
            b.append(p)
    return a if len(a) else b

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

    print(score_for_deck(get_winning_deck(a, b)))

main()
