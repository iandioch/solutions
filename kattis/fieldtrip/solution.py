def main():
    n = int(input())
    sizes = list(map(int, input().split()))
    tot = sum(sizes)

    bus = tot // 3
    if bus*3 < tot:
        print(-1)
        return


    curr = 0
    a = -1
    for i in range(n):
        if curr + sizes[i] > bus:
            print(-1)
            return
        if curr + sizes[i] == bus:
            a = i
            break

        curr += sizes[i]

    curr = 0
    b = -1
    for i in range(a+1, n):
        if curr + sizes[i] > bus:
            print(-1)
            return
        if curr+sizes[i] == bus:
            b = i
            break
        curr += sizes[i]
    if b < 0:
        print(-1)
    else:
        print(a+1,b+1)

main()
