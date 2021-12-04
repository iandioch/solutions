def valid(num):
    num_str = str(num)
    num_in_row = [1]
    for i in range(1, len(num_str)):
        if num_str[i-1] == num_str[i]:
            num_in_row.append(num_in_row[-1] + 1)
        else:
            num_in_row.append(1)
        if ord(num_str[i-1]) > ord(num_str[i]):
            return False

    for i in range(len(num_in_row)):
        if num_in_row[i] == 2:
            if i == len(num_in_row) - 1:
                return True
            if num_in_row[i+1] == 1:
                return True
    return False


def main():
    lo, hi = map(int, input().split('-'))
    print(sum(1 for num in range(lo, hi+1) if valid(num)))

main()
