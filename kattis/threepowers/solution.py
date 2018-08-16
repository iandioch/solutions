def main():

    threepows = [1]
    while len(threepows) < 64:
        threepows.append(threepows[-1]*3)
    while True:
        n = int(input())
        if n == 0:
            break
        n -= 1
        out = []
        for i in range(len(threepows)):
            if (1<<i) & n:
                out.append(str(threepows[i]))

        print('{ ' + ', '.join(out) + ' }')

if __name__ == '__main__':
    main()
