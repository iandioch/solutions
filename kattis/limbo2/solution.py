def main():
    n = int(input())
    for _ in range(n):
        r, c = map(int, input().split())
        h = 1
        hgrow = 0
        while r >= h:
            h *= 2
            hgrow += 2
        w = 1
        wgrow = 0
        while c >= w:
            w *= 2
            if (wgrow == 0):
                wgrow = 1
            else:
                wgrow += 2
        iteration = max(hgrow, wgrow)
        if iteration == 0:
            print(0)
            continue
        first = 2**(iteration-1)
        #print("first =", first, "iteration =", iteration)
        if iteration % 2 == 1:
            # was a new block to the right
            stripe_size = 2**(iteration//2) # num new blocks in a stripe
            #print("stripe", stripe_size)
            prev_width = stripe_size
            #print("prev width", prev_width)
            n = c - prev_width 
            print(first + stripe_size*n + r)
        else:
            # was a new block below 
            stripe_size = 2**(iteration//2)
            prev_height = stripe_size//2
            #print("stripe", stripe_size)
            n = r - prev_height 
            print(first + stripe_size*n + c)

if __name__ == '__main__':
    main()
