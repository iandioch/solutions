def main():
    a = input()
    op = input()
    b = input()

    # Ensure a >= b
    if len(b) > len(a):
        a, b = b, a
    if op == '+':
        if len(a) == len(b):
            print('2' + '0'*(len(a)-1))
            return
        ans = [c for c in a]
        ans[-len(b)] = '1'
        print(''.join(ans))
        return

    print('1' + '0'*(len(a)-1 + len(b)-1))

main()
