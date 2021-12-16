def bits_to_int(bit_list):
    return int(''.join(map(str, bit_list)), 2)

def yield_bits(s):
    for c in s:
        yield from (int(d) for d in format(int(c, 16), '04b'))

TOT_VERSION = 0
def parse(bits, ptr=0):
    global TOT_VERSION

    def parse_number():
        nonlocal ptr
        num = 0
        while True:
            is_last = (bits[ptr] == 0)
            ptr += 1
            for i in range(4):
                num *= 2
                num += bits[ptr]
                ptr += 1

            if is_last:
                break
        return num

    def parse_operator():
        nonlocal ptr
        length_type_id = bits[ptr]
        ptr += 1

        subpackets = []
        if length_type_id == 0:
            # num = total length in bits of subpackets
            num = bits_to_int(bits[ptr:ptr+15])
            ptr += 15
            print(ptr, 'number of bits of subpackets', num)

            final_ptr = ptr + num
            while ptr < final_ptr:
                new_ptr, res = parse(bits, ptr)
                ptr = new_ptr
                subpackets.append(res)
        else:
            # num = number of subpackets
            num = bits_to_int(bits[ptr:ptr+11])
            ptr += 11
            print(ptr, 'number of subpackets', num)
            for _ in range(num):
                new_ptr, res = parse(bits, ptr)
                ptr = new_ptr
                subpackets.append(res)
        print(ptr, 'end of operator packet', subpackets)
        return subpackets[-1]

    orig_ptr = ptr
    version = bits_to_int(bits[ptr:ptr+3])
    ptr += 3
    print(ptr, 'version', version)
    TOT_VERSION += version
    type_id = bits_to_int(bits[ptr:ptr+3])
    ptr += 3
    print(ptr, 'type_id', type_id)

    result = None
    if (type_id == 4):
        result = parse_number()
        print(ptr, 'number', result)
    else:
        result = parse_operator()
        print(ptr, 'operator', result)

    return ptr, result


def main():
    parse(list(yield_bits(input())))
    print(TOT_VERSION)

main()
