def intersects(x1, y1, x2, y2, x3, y3, x4, y4):
    denom = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
    if denom == 0:
        return False
    x = (((y1 - y3) * (x4 - x3)) - ((x1 - x3) * (y4 - y3))) / denom
    y = (((y1 - y3) * (x2 - x1)) - ((x1 - x3) * (y2 - y1))) / denom
    return (x >= 0 and x <= 1) and (y >= 0 and y <= 1)

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        lines = []
        for _ in range(n):
            a, b, c, d = map(float, input().split())
            lines.append((a, b, c, d))
        ans = 0
        for i in range(n-2):
            x1, y1, x2, y2 = lines[i]
            for j in range(i+1, n-1):
                x3, y3, x4, y4 = lines[j]
                if not intersects(x1, y1, x2, y2, x3, y3, x4, y4):
                    continue
                for k in range(j+1, n):
                    a, b, c, d = lines[k]
                    if not intersects(x1, y1, x2, y2, a, b, c, d):
                        continue
                    if intersects(x3, y3, x4, y4, a, b, c, d):
                        ans += 1
        print(ans)

if __name__ == '__main__':
    main()
