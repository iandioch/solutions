def main():
    n = int(input())
    tot = 0
    prevx, prevy = map(float, input().split())
    for i in range(1, n):
        x, y = map(float, input().split())
        tot += min(y, prevy)*(x-prevx)
        tot += 0.5*(x-prevx)*(max(y, prevy)-min(y, prevy))
        prevx = x
        prevy = y
    print(tot/1000)

if __name__ == '__main__':
    main()
