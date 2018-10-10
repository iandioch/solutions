from math import log, ceil

def main():
    n = int(input())
    for _ in range(n):
        a = int(input())
        tot = 2**a
        # every time we div by 2 and mult by 11, it should add a digit

        num11 = 0
        while ceil(log(tot, 10)) < a:
            tot //= 2
            tot *= 11
            num11 += 1
        num2 = a - num11
        print(("2 "*num2) + ("11 "*num11))

if __name__ == '__main__':
    main()
