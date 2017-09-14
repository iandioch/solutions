while True:
    s = input()
    if s == '0':
        break
    keylen, *key = map(int, s.split())
    message = input()
    output = ''
    while len(message) % keylen != 0:
        message += ' '
    i = 0
    while i < len(message):
        t = message[i:i+keylen]
        output += ''.join([t[j-1] for j in key])
        i += keylen
    print("'{}'".format(output))
