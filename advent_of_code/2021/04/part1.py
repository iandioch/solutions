import sys

def main():
    balls = list(map(int, input().split(',')))
    lines = [l.strip() for l in sys.stdin.readlines()]

    boards = []
    for i in range(0, len(lines), 6):
        boards.append([list(map(int, lines[j].split())) for j in range(i+1, i+6)])

    def emit_winning_board(board, num_set, last_ball):
        unmarked = 0
        for row in board:
            unmarked += sum(num for num in row if num not in num_set)
        tot = unmarked * last_ball
        print(tot)

    num_set = set()
    for ball in balls:
        num_set.add(ball)
        for board in boards:
            for row in board:
                if all(num in num_set for num in row):
                    emit_winning_board(board, num_set, ball)
                    return
            for i in range(5):
                if all(b[i] in num_set for b in board):
                    emit_winning_board(board, num_set, ball)
                    return

main()
