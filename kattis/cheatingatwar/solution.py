def solve(mine, opp):
    from collections import defaultdict
    cards = defaultdict(int)
    for c in mine:
        cards[c] += 1
    beaten = set()
    currdiff = 1
    while len(beaten) < 26:
        found_one = False
        for i in range(26):
            if i in beaten:
                continue
            if cards[opp[i] + currdiff] >= 1:
                cards[opp[i] + currdiff] -= 1
                beaten.add(i)
                found_one = True
        if not found_one:
            currdiff += 1
            if currdiff > 13:
                drawn = 0
                for i in range(26):
                    if i in beaten:
                        continue
                    if cards[opp[i]] >= 1:
                        drawn += 1
                        cards[opp[i]] -= 1
                return len(beaten)*2 + drawn
    return 26*2

def main():
    cards = '23456789TJQKA'
    value = {card:cards.index(card) for card in cards}
    n = int(input())
    for _ in range(n):
        opp = [value[c] for c in input()]
        mine = [value[c] for c in input()]
        print(solve(mine, opp))

main()
