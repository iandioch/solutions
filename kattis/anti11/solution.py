from functools import lru_cache

@lru_cache(maxsize=None)
def solve(v):
    if v == 1:
        return 2 # 0, 1
    if v == 2:
        return 3 # 10, 01, 00
    if v == 3:
        return 5 # 000, 001, 010, 100, 101
    if v == 4:
        return 8 # 0000, 0001, 0010, 0100, 0101, 1000, 1001, 1010
    return solve(v-1) + solve(v-2)

def main():
    n = int(input())
    for _ in range(n):
        print(solve(int(input())) % (10**9 + 7))

main()
