n = int(input())

length = 0
while True:
    length += 1
    num_at_length = 2**((length-1)//2)
    if num_at_length >= n:
        # Palindrome is of length `length`.
        pal = '1'
        s = ''
        if length > 2:
            s = bin(n-1)[2:].zfill((length-1)//2)
        b = pal + s + s[::-1] + pal
        if length % 2 == 1:
            b = b[:len(b)//2] + b[len(b)//2+1:]
        ans = int(b, 2)
        print(ans)
        break
    n -= num_at_length
