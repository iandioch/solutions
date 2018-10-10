def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    ans = []

    def swap(i):
        if (i == 0):
            return
        nonlocal a
        ans.append(i)
        a = a[i:] + a[:i][::-1]

    while True:
        curr = 1 
        for i in range(a.index(1), n-1):
            if a[i + 1] != curr + 1:
                break
            curr += 1
        if curr == n:
            break
        # reverse the list
        swap(n)
        if (a.index(curr)) > 0:
            swap(a.index(curr))
        swap(a.index(1)+1)
        swap(a.index(curr+1)+1)

    print(len(ans))
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
