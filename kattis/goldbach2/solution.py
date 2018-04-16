def main():
    is_prime = [True for _ in range(32005)]
    primes = []
    for i in range(2, 32005):
        if is_prime[i]:
            primes.append(i)
            for j in range(i+i, 32005, i):
                is_prime[j] = False
    n = int(input())
    for _ in range(n):
        m = int(input())
        ans = []
        i, j = 0, 0
        while j < len(primes) and primes[j] < m:
            j += 1
        while i <= j:
            if primes[i] + primes[j] == m:
                ans.append((primes[i], primes[j]))
                i += 1
            elif primes[i] + primes[j] > m:
                j -= 1
            else:
                i += 1
        print('{} has {} representation(s)'.format(m, len(ans)))
        for a, b in ans:
            print('{}+{}'.format(a,b))
        print()

if __name__ == '__main__':
    main()
