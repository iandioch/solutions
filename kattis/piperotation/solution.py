def main():
    h, w = map(int, input().split())
    board = [input() for _ in range(h)]
    #print(board)
    reqright = [[False for _ in range(w)] for _ in range(h)]
    reqbottom = [[False for _ in range(w)] for _ in range(h)]

    for i in range(w):
        for j in range(h):
            #print(i, j)
            r = reqright[j][i-1] if i > 0 else False
            b = reqbottom[j-1][i] if j > 0 else False
            c = board[j][i]
            if c == 'A':
                # empty
                if r or b:
                    print('Impossible')
                    return
                reqright[j][i] = False
                reqbottom[j][i] = False
            elif c == 'B':
                # straight
                if r == b:
                    print('Impossible')
                    return
                reqright[j][i] = r
                reqbottom[j][i] = b
            elif c == 'C':
                # corner
                reqright[j][i] = not r
                reqbottom[j][i] = not b
            elif c == 'D':
                # 4-way/cross
                if not (r and b):
                    print('Impossible')
                    return
                reqright[j][i] = True
                reqbottom[j][i] = True
    for i in range(w):
        if reqbottom[h-1][i]:
            print('Impossible')
            return
    for j in range(h):
        if reqright[j][w-1]:
            print('Impossible')
            return
    print('Possible')

if __name__ == '__main__':
    main()
