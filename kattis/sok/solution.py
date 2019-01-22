def main():
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    minq = min(x[i]/y[i] for i in range(3))
    print(*(x[i] - minq*y[i] for i in range(3)))

if __name__ == '__main__':
    main()
