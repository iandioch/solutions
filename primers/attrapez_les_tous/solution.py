import random
import sys


def make_set(moves, names):
    best_size = 0
    bests = set([0])
    best_set = set(moves[names[0]])

    while len(bests) < 6:
        best_index = -1 
        best_size = 0
        for i in range(len(names)):
            if i in bests:
                continue
            comb = best_set | moves[names[i]]
            if len(comb) >= best_size:
                best_size = len(comb)
                best_index = i
        bests.add(best_index)
        best_set |= moves[names[best_index]]

    return [names[i] for i in bests], best_set

def main():
    moves = {}
    names = []

    for line in sys.stdin.readlines():
        pname, *pmoves = line.strip().split(',')
        pmoves = set(map(int, pmoves))
        moves[pname] = pmoves
        names.append(pname)

    best_names = []
    best_moveset = set()
    for _ in range(250):
        random.shuffle(names)
        chosen_names, moveset = make_set(moves, names)
        if len(moveset) > len(best_moveset):
            best_moveset = moveset
            best_names = chosen_names
            print('-'*5)
            print('Score:', len(best_moveset))
            print('\n'.join(best_names))
            print('-'*5)


main()
