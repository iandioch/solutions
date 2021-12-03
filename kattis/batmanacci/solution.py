def main():
    n, k = map(int, input().split())

    fib = [0, 1, 1]
    for _ in range(n + 1):
        fib.append(fib[-1] + fib[-2])

    while n > 2:
        # Figure out if k is in the first or second part of the concatenation,
        # and then "zoom in" on just that part.
        if k > fib[n-2]:
            k -= fib[n-2]
            n -= 1
        else:
            n -= 2
    print("XNA"[n])

main()
