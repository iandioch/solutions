import math
import time
import random
import heapq
from collections import deque

GATE_DISTS = []
TRANSFERS = []
BEST_COST = 9999999999
BEST_ARRANGEMENT = []

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

def gen_neighbour(arrangement):
    i = random.randrange(0, len(arrangement))
    j = i
    while j == i:
        j = random.randrange(0, len(arrangement))
    arr = arrangement[:]
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def simulated_annealing(arrangement):
    MAX_ITER = 999999

    def temperature(step):
        return 1 - (step+1) / MAX_ITER

    def prob(energy, neighbour_energy, temperature):
        if neighbour_energy < energy:
            return 1
        return math.exp(-(neighbour_energy - energy)/temperature)

    for step in range(MAX_ITER):
        temp = temperature(step)
        energy = cost_of_arrangement(arrangement)
        emit_arrangement(arrangement, energy, title=f'step[{step}]')
        neighbour = gen_neighbour(arrangement)
        if prob(energy, cost_of_arrangement(neighbour), temp) >= random.random():
            arrangement = neighbour

def main():
    global TRANSFERS, GATE_DISTS

    n = int(input())
    GATE_DISTS = [list(map(int, input().split(','))) for _ in range(n)]
    TRANSFERS = [list(map(int, input().split(','))) for _ in range(n)]

    initial_state = list(range(n))
    random.shuffle(initial_state)

    simulated_annealing(initial_state)

    iter_queue()

main()
