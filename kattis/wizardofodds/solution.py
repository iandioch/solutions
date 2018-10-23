def main():
    n, k = map(int, input().split())
    if (k >= 400) or (2**k >= n):
        print('Your wish is granted!')
    else:
        print('You will become a flying monkey!')

if __name__ == '__main__':
    main()
