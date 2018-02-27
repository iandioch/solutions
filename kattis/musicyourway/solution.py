attrs = input().split()
n_songs = int(input())
songs = [input().split() for _ in range(n_songs)]
n = int(input())
for _ in range(n):
    k = input().strip()
    v = attrs.index(k)
    songs = sorted(songs, key=lambda x:x[v])
    print(' '.join(attrs))
    for s in songs:
        print(' '.join(s))
    print()
