import time
import random
import heapq
from collections import deque

GATE_DISTS = []
TRANSFERS = []
BEST_COST = 999999999 
BEST_ARRANGEMENT = []
QUEUE = [] #deque()

def time_str():
    return '[' + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + ']'

def emit_arrangement(arr, cost, title=''):
    global BEST_COST, BEST_ARRANGEMENT
    if cost >= BEST_COST:
        return
    BEST_COST = cost
    BEST_ARRANGEMENT = arr
    print('-'*10)
    print(f'{title} @ cost {cost}:')
    print('\n'.join(map(lambda g: str(g+1), arr)))
    print(time_str(), 'cost:', cost)
    print('-'*10)

def cost_of_arrangement(arrangement):
    cost = 0
    for i in range(len(arrangement)):
        flight = arrangement[i]
        if flight < 0:
            continue
        for j in range(len(arrangement)):
            if i == j:
                continue
            other_flight = arrangement[j]
            if other_flight < 0:
                continue
            gate_dist = GATE_DISTS[i][j]
            traffic = TRANSFERS[flight][other_flight]
            cost += gate_dist*traffic
    return cost

def cmp(flight_a, flight_b):
    return -TRANSFERS[flight_a][flight_b]

def add_flight(arrangement, unused_gate_indices, unused_flight_indices):
    if not len(unused_flight_indices):
        emit_arrangement(arrangement, cost_of_arrangement(arrangement))
        return

    value = (0, 0)
    if True or len(QUEUE) < 1000:
        value = (len(unused_flight_indices), cost_of_arrangement(arrangement))
    heapq.heappush(QUEUE, (value, arrangement, unused_gate_indices, unused_flight_indices))

    """
    if len(QUEUE) < 1000:
        QUEUE.append((arrangement, unused_gate_indices, unused_flight_indices))
    else:
        QUEUE.appendleft((arrangement, unused_gate_indices, unused_flight_indices))
        """


def iter_queue():
    iter_n = 0
    while len(QUEUE):
        iter_n += 1
        heap_sorter, arrangement, unused_gate_indices, unused_flight_indices = heapq.heappop(QUEUE)# QUEUE.popleft()

        cost_of_arr = cost_of_arrangement(arrangement)
        if cost_of_arr > BEST_COST:
            continue 

        if iter_n % 100 == 0:
            print(f'{time_str()} Curr queue length: {len(QUEUE)}, curr best score {BEST_COST}.')
            print(f'Front of queue: cost {cost_of_arr} with {len(unused_flight_indices)} flights not placed.')

        def optimal_single_additions():
            NUM_TO_CONSIDER_PER_GATE = 3
            NUM_TO_CONSIDER_TOTAL = 2
            open_spot = []
            for i in range(len(arrangement)-1):
                if arrangement[i] < 0 and arrangement[i+1] >= 0:
                    open_spot.append(i)
                elif arrangement[i] >= 0 and arrangement[i+1] < 0:
                    open_spot.append(i+1)

            # list of (cost, gate, flight) tuples
            poss = []
            for gate in open_spot:
                left_dist, right_dist = 0, 0
                left_flight = -1
                right_flight = -1
                if gate > 0 and arrangement[gate-1] >= 0:
                    left_dist = GATE_DISTS[gate][gate-1]
                    left_flight = arrangement[gate-1]
                if gate < len(arrangement)-1 and arrangement[gate+1] >= 0:
                    right_dist = GATE_DISTS[gate][gate+1]
                    right_flight = arrangement[gate+1]

                def cost(flight):
                    n = 0
                    if left_dist > 0:
                        n += left_dist * TRANSFERS[left_flight][flight]
                        n += left_dist * TRANSFERS[flight][left_flight]
                    if right_dist > 0:
                        n += right_dist * TRANSFERS[right_flight][flight]
                        n += right_dist * TRANSFERS[flight][right_flight]
                    return n
                poss_flights = sorted(unused_flight_indices, key=cost)
                for f in poss_flights[:min(len(poss_flights), NUM_TO_CONSIDER_PER_GATE)]:
                    poss.append((cost(f), gate, f))
            poss.sort()
            for (cost, gate, flight) in poss[:min(len(poss), NUM_TO_CONSIDER_TOTAL)]:
                arr = arrangement[:]
                arr[gate] = flight
                unused_gates = set(unused_gate_indices)
                unused_gates.remove(gate)
                unused_flights = set(unused_flight_indices)
                unused_flights.remove(flight)
                add_flight(arr, unused_gates, unused_flights)

        optimal_single_additions()


def main():
    global TRANSFERS, GATE_DISTS

    n = int(input())
    GATE_DISTS = [list(map(int, input().split(','))) for _ in range(n)]
    TRANSFERS = [list(map(int, input().split(','))) for _ in range(n)]


    empty_arrangement = [-1 for _ in range(n)]
    NUM_RAND_INITIAL_STATES = 1000
    for i in range(NUM_RAND_INITIAL_STATES):
        arr = empty_arrangement[:]
        gate = random.randint(0, n-1)
        flight = random.randint(0, n-1)
        print(f'... Considering new initial state: {flight} at {gate} ...')
        arr[gate]=flight
        unused_gates = set(range(n))
        unused_gates.remove(gate)
        unused_flights = set(range(n))
        unused_flights.remove(flight)
        add_flight(arr, unused_gates, unused_flights)

    iter_queue()

main()
