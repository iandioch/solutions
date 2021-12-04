from collections import defaultdict

def main():
    centre_letter, *other_letters = input()
    available = set([centre_letter] + other_letters)
    n = int(input())
    for _ in range(n):
        word = input()
        if len(word) < 4:
            continue
        letters = set(word)
        if centre_letter not in letters:
            continue
        valid = (letters <= available)
        if valid:
            print(word)

main()
