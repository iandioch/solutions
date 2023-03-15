def is_multigram(s, n):
    #print(':', s, n)
    if len(s) % n != 0:
        return False
    t = sorted(s[:n])
    for i in range(1, len(s)//n):
        p = s[i*n:i*n+n]
        #print(i, t, p, sorted(p))
        if sorted(p) != t:
            return False
    return True

def main():
    s = input()
    for n in range(1, len(s)//2+1):
        if is_multigram(s, n):
            print(''.join(s[:n]))
            return
    print('-1')

main()
