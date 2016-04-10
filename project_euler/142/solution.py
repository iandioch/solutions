limit = 1000

squares = []

for i in xrange(1, limit):
    squares.append(i*i)

square_set = set(squares)
ans = 1000000000
for a in squares:
    for c in squares:
        f = a - c
        if f <= 0 or not f in square_set:
            continue
        
        for d in squares:
            e = a - d
            b = c - e
            if e < 0 or b < 0:
                continue
            if not (e in square_set and b in square_set):
                continue
            

            
            x = (c+d)/2
            y = (2*a - d - c)/2
            z = (c-d)/2
            if z < 0 or x < 0 or y < 0:
                continue
            if (z*2 != c - d) or (y*2 != 2*a - d - c) or (x*2 != c + d):
                continue
            n = x + y + z
            if n > ans:
                break
            ans = n
            print x, y, z, ans

print ans
