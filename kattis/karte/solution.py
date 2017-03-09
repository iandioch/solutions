s = input()

suits = {}
suit_names = 'PKHT'
for suit in suit_names:
    suits[suit] = set()

done = False

for i in range(0, len(s), 3):
    suit = s[i]
    face = s[i+1:i+3]
    if face in suits[suit]:
        print('GRESKA')
        done = True
        break
    suits[suit].add(face)

if not done:
    for suit in suit_names:
        print(13-len(suits[suit]), end=' ')
print()
