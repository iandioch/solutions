def p(s):
    print(s, end='')

line = input()

for i in range(len(line)):
    star = (i+1) % 3 == 0
    if i == 0:
        p('.')
    if star:
        p('.*.')
    else:
        p('.#.')
    #if i == len(line)-1:
    p('.')
print()

for i in range(len(line)):
    star = (i+1) % 3 == 0
    if star:
        p('.*.*')
    else:
        p('.#.#')
print('.')

for i in range(len(line)):
    star = (i+1) % 3 == 0 or (i>0 and i % 3 == 0)
    if star:
        p('*.' + line[i] + '.')
    else:
        p('#.' + line[i] + '.')
if len(line) % 3 == 0:
    print('*')
else:
    print('#')

for i in range(len(line)):
    star = (i+1) % 3 == 0
    if star:
        p('.*.*')
    else:
        p('.#.#')
print('.')

for i in range(len(line)):
    star = (i+1) % 3 == 0
    if i == 0:
        p('.')
    if star:
        p('.*.')
    else:
        p('.#.')
    #if i == len(line)-1:
    p('.')
print()
