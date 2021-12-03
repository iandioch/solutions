def is_correct():
    n = int(input())
    queens = [list(map(int, input().split())) for _ in range(n)]
    for i in range(len(queens)):
        x, y = queens[i]
        for j in range(i+1, len(queens)):
            p, q = queens[j]
            if p == x or q == y:
                return False
            if (x+y) == (p+q) or (x-y) == (p-q):
                return False
    return True


def main():
    print('CORRECT' if is_correct() else 'INCORRECT')

main()
