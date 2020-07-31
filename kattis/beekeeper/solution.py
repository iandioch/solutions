def main():
    vowels = set('aeiouy')

    while True:
        n = int(input())
        if n == 0:
            break
        best = -1
        best_word = "none"
        for _ in range(n):
            word = input()
            c = 0
            for i in range(1, len(word)):
                if word[i] == word[i-1]:
                    if word[i] in vowels:
                        c += 1
            if c > best:
                best = c
                best_word = word
        print(best_word)

main()
