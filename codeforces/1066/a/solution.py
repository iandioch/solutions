def main():
    t = int(input())
    for _ in range(t):
        L, v, l, r = map(int, input().split())
        numbefore = (l-1)//v
        numduring = r//v
        numafter = L//v
        print (numafter - (numduring - numbefore))

if __name__ == '__main__':
    main()
