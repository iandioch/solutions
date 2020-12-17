def main():
    from math import factorial
    n = int(input())
    print(sum(1/factorial(i) for i in range(min(n+1, 20))))

main()
