def main():
    n = int(input())
    for _ in range(n):
        id_, v = input().split()
        v = int(v)
        print(id_, (v*(v+1))//2 + v)

main()
