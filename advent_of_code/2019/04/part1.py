def valid(num):
    num_str = str(num)
    double = False
    for i in range(len(num_str)-1):
        double = double or (num_str[i] == num_str[i+1])
        if ord(num_str[i]) > ord(num_str[i+1]):
            return False
    return double


def main():
    lo, hi = map(int, input().split('-'))
    print(sum(1 for num in range(lo, hi+1) if valid(num)))

main()
