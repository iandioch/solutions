import sys

def validate_field(field, value):
    try:
        if field == 'byr':
            v = int(value)
            return v >= 1920 and v <= 2002
        elif field == 'iyr':
            v = int(value)
            return v >= 2010 and v <= 2020
        elif field == 'eyr':
            v = int(value)
            return v  >= 2020 and v <= 2030
        elif field == 'hgt':
            if value.endswith('cm'):
                v = int(value[:-2])
                return v >= 150 and v <= 193
            elif value.endswith('in'):
                v = int(value[:-2])
                return v >= 59 and v <= 76
            else:
                print('unrecognised unit', value)
                return False
        elif field == 'hcl':
            if value[0] != '#':
                return False
            return all(c in '0123456789abcdef' for c in value[1:])
        elif field == 'ecl':
            return value in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
        elif field == 'pid':
            if len(value) != 9:
                return False
            return all(c in '0123456789' for c in value)
        elif field == 'cid':
            return True
        else:
            print('unrecognised field', field)
            return False

    except Exception as e:
        return False

def validate(passport):
    print('checking passport')
    print(passport)
    print('----')
    req_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    for line in passport:
        parts = line.split(' ')
        for p in parts:
            field, value = p.split(':')
            req_fields.discard(field)
            if not validate_field(field, value):
                return False
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
