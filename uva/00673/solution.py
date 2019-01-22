from collections import deque
def test(s):
    d = deque()
    for c in s:
        if c == '(' or c == '[':
            d.append(c)
        else:
            if len(d) == 0:
                return False
            curr = d.pop()
            ok = (c == ']' and curr == '[') or (c == ')' and curr == '(')
            if not ok:
                return False
    return (len(d) == 0)
    
def main():
    n = int(input())
    for _ in range(n):
        s = input()
        ok = test(s)
        print('Yes' if ok else 'No')

if __name__ == '__main__':
    main()
