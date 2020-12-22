def main():
    r, c = map(int, input().split())
    east = list(map(int, input().split()))
    north = list(map(int, input().split()))
    poss = max(east) == max(north)
    if poss:
        print('possible')
    else:
        print('impossible')
        
main()
