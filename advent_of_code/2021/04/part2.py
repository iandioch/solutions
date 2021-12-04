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

    won = []
    won_set = set()
    for ball in balls:
        num_set.add(ball)
        for board_num, board in enumerate(boards):
            if board_num in won_set:
                continue
            for row in board:
                if all(num in num_set for num in row):
                    won_set.add(board_num)
                    won.append((board_num, ball, set(num_set)))
            for i in range(5):
                if all(b[i] in num_set for b in board):
                    won_set.add(board_num)
                    won.append((board_num, ball, set(num_set)))


    winning_board, last_ball, all_balls = won[-1]
    emit_winning_board(boards[winning_board], all_balls, last_ball)

main()
