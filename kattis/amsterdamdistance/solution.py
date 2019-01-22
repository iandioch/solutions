import math

def circdist(rad, totring, totslice, ringno, a, b):
    # a < b
    r = (ringno/totring)*rad
    fullcirc = 2*math.pi*r
    thiscirc = (fullcirc/2)*((b-a)/totslice)
    return thiscirc

def main():
    numslice, numring, rad = input().split()
    numslice = int(numslice)
    numring = int(numring)
    rad = float(rad)
    ax, ay, bx, by = map(int, input().split())
    miny, maxy = min(ay, by), max(ay, by)
    minx, maxx = min(ax, bx), max(ax, bx)
    best = rad*100
    for i in range(0, maxy+1):
        n = circdist(rad, numring, numslice, i, minx, maxx)
        m = (abs(maxy-i)/numring)*rad + (abs(i-miny)/numring)*rad
        best = min(best, n+m)
    print(best)

if __name__ == '__main__':
    main()
