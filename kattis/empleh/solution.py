white = input().split(':')[1].strip().split(',')
black = input().split(':')[1].strip().split(',')
board = [[None for _ in range(8)] for _ in range(8)]

for p in white:
    if not len(p):
        continue
    x, y = 0, 0
    symbol = None
    if p[0].upper() == p[0]:
        # not a pawn
        y = int(p[-1]) - 1
        x = ord(p[1]) - ord('a')
        symbol = p[0]
    else:
        y = int(p[-1]) - 1
        x = ord(p[0]) - ord('a')
        symbol = 'P'
    board[y][x] = symbol

for p in black:
    if not len(p):
        continue
    x, y = 0, 0
    symbol = None
    if p[0].upper() == p[0]:
        # not a pawn
        y = int(p[-1]) - 1
        x = ord(p[1]) - ord('a')
        symbol = p[0].lower()
    else:
        y = int(p[-1]) - 1
        x = ord(p[0]) - ord('a')
        symbol = 'p'
    board[y][x] = symbol

for y in range(7, -1, -1):
    print('+---'*8 + '+')
    for x in range(8):
        fill = '.' if ((x+y)%2 == 1) else ':'
        print('|', end='')
        if board[y][x] is None:
            print(fill*3, end='')
        else:
            print(fill + board[y][x] + fill, end='')
    print('|')
print('+---'*8 + '+')
