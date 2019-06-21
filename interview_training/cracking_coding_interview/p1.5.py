def op(a, b):
    al = len(a)
    bl = len(b)

    def check_if_del_1(shorter, longer, shorter_l, longer_l):
        i, j = 0, 0
        ndel = 0
        while i < shorter_l and j < longer_l and ndel <= 1:
            if shorter[i] == longer[j]:
                i += 1
                j += 1
            else:
                j += 1
                ndel += 1
        return ndel <= 1 and i == shorter_l 
    if al == bl:
        # Check if only one letter is diff
        ndiff = 0
        for c, d in zip(a, b):
            if c != d:
                ndiff += 1
                if ndiff > 1:
                    return False
        return True
    elif al == bl - 1:
        # Check if you can del a letter from b
        return check_if_del_1(a, b, al, bl)
    elif al == bl + 1:
        # Check if you can del a letter from a
        return check_if_del_1(b, a, bl, al)
    else:
        return False

def main():
    a, b = input().split()
    print(op(a, b))

if __name__ == '__main__':
    main()
