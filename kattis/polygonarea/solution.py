def signed_shoelace(x, y, n):
    a, b = 0, 0
    for i in range(n-1):
        a += (x[i] * y[i+1])
        b += (y[i] * x[i+1])
    a += x[n-1] * y[0]
    b += y[n-1] * x[0]
    return (a-b)/2.0

def main():
    x = [0]*1001
    y = [0]*1001
    while True:
        n = int(input())
        if n == 0:
            break
        for i in range(n):
            x[i], y[i] = map(int, input().split())
        a = signed_shoelace(x, y, n)
        cw = 'CW' if a <= 0 else 'CCW'
        print('{} {:.1f}'.format(cw, abs(a)))




if __name__ == '__main__':
    main()
