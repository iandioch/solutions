def main():
    n, r = map(int, input().split())
    arr = [True if c == '1' else False for c in input().split()]
    #print(arr)

    last_heated = 0
    tot = 0
    last_turned = -1
    while last_heated < n:
        optim = last_heated + r - 1

        while True:
            if optim < 0:
                print('-1')
                return
            if optim <= last_turned:
                print('-1')
                return
            if optim >= n:
                optim -= 1
                continue
            if arr[optim]:
                # found a heater
                tot += 1
                last_heated = optim + r
                last_turned = optim
                #print('turn on ' + str(optim))
                break
            optim -= 1
    print(tot)


if __name__ == '__main__':
    main()
