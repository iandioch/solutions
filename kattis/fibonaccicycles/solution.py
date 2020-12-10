def main():
    q = int(input())
    for _ in range(q):
        k = int(input())
        seen = {}
        a = 2%k # F(2)
        b = 3%k # F(3)
        n = 2
        #print('F(0) = 1')
        #print('F(1) = 1')
        while (a%k) not in seen:#a not in seen:
            seen[a%k] = n
            #print('F({}) = {}'.format(n, a))
            a, b = b, (a+b)
            n += 1
        print(seen[a%k])

main()
