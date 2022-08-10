import time

GATE_DISTS = []
TRANSFERS = []
BEST_COST = 99999999999
BEST_ARRANGEMENT = []

def emit_arrangement(arr, cost, title=''):
    print('-'*10)
    print(f'{title} @ cost {cost}:')
    print('\n'.join(map(lambda g: str(g+1), arr)))
    print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()), 'cost:', cost)
    print('-'*10)

def cost_of_arrangement(arrangement):
    cost = 0
    for i in range(len(arrangement)):
        flight = arrangement[i]
        for j in range(len(arrangement)):
            if i == j:
                continue
            other_flight = arrangement[j]
            gate_dist = GATE_DISTS[i][j]
            traffic = TRANSFERS[flight][other_flight]
            cost += gate_dist*traffic
    return cost

def cmp(flight_a, flight_b):
    return -TRANSFERS[flight_a][flight_b]

def add_flight(arrangement, unused_flight_indices, num_considered_flights=2):
    if not len(unused_flight_indices):
        return arrangement, cost_of_arrangement(arrangement)

    best_cost = 9999999999
    best_arrangement = []
    def consider_poss(arr, cost):
        nonlocal best_cost, best_arrangement
        if cost < best_cost:
            best_cost = cost
            best_arrangement = arr

        global BEST_COST, BEST_ARRANGEMENT
        if cost < BEST_COST:
            BEST_COST = cost
            BEST_ARRANGEMENT = arr
            emit_arrangement(arr, cost, title='new best')

    prefix_flights = sorted(unused_flight_indices, key=lambda f:cmp(arrangement[0], f))
    for i in range(min(len(prefix_flights), num_considered_flights)):
        poss_arr = [prefix_flights[i]] + arrangement
        poss_unused = set(unused_flight_indices)
        poss_unused.remove(prefix_flights[i])
        consider_poss(*add_flight(poss_arr, poss_unused, num_considered_flights))
    return best_arrangement, best_cost


def main():
    global TRANSFERS, GATE_DISTS

    n = int(input())
    GATE_DISTS = [list(map(int, input().split(','))) for _ in range(n)]
    TRANSFERS = [list(map(int, input().split(','))) for _ in range(n)]

    best_cost = 99999999999
    best_arrangement = []
    for i in range(n):
        unused = set(range(n))
        unused.remove(i)
        arr, cost = add_flight([i], unused)
        if cost < best_cost:
            best_cost = cost
            best_arrangement = arr
            emit_arrangement(arr, cost, title='new best for starting flight' + str(i+1))
    emit_arrangement(best_arrangement, best_cost, title='overall best')


main()
