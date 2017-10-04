n = int(input())
a = input()
b = input()
trans = str.maketrans('01', '10')
if n % 2 == 1:
    a = a.translate(trans)
if a == b:
    print('Deletion succeeded')
else:
    print('Deletion failed')
