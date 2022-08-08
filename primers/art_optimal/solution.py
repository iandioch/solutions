def main():
    w, h = map(int, input().split(','))
    lines = [[(c == '#') for c in input().strip()] for _ in range(h)]
    for j in range(h):
        #print(''.join(('#' if c else '*') for c in lines[j]))
        for i in range(w):
            if lines[j][i]:
                print(f'FILL,{i},{j},1')

main()
