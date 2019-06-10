def isrot(s1, s2):
    return s1 in (s2 + s2)

if __name__ == '__main__':
    s1, s2 = input().split()
    print(isrot(s1, s2))
