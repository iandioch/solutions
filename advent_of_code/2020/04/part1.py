import sys

def validate(passport):
    print('checking passport')
    print(passport)
    print('----')
    req_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    for line in passport:
        parts = line.split(' ')
        for p in parts:
            pid = p.split(':')[0]
            req_fields.discard(pid)
    return len(req_fields) == 0

ans = 0
curr_passport = []
for line in sys.stdin.readlines():
    line = line.strip()
    if line == '':
        if validate(curr_passport):
            ans += 1
        curr_passport = []
    else:
        curr_passport.append(line)

# there might not be an empty last line, so we need to check the last passport
if validate(curr_passport):
    ans += 1

print(ans)
