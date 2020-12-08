import sys

def interpret(program, seen, acc, ip, can_change):
    target_line = len(program)
    while True:
        if ip in seen:
            return None
        seen.add(ip)
        if ip == target_line:
            return acc

        instruction = program[ip][0]
        if instruction == 'acc':
            acc += int(program[ip][1])
            ip += 1
            continue
        elif instruction == 'jmp':
            if can_change:
                # See if this was a nop, would it work
                modified_program = program[:]
                seen_copy = set(seen)
                poss_result = interpret(modified_program, seen_copy, acc,
                                        ip+1, False)
                if poss_result is not None:
                    return poss_result

            # Usual case, this is a jmp and not a nop
            ip += int(program[ip][1])
            continue
        elif instruction == 'nop':
            if can_change:
                # See if this was a jmp, would it work
                modified_program = program[:]
                seen_copy = set(seen)
                poss_result = interpret(modified_program, seen_copy, acc,
                                        ip+int(program[ip][1]), False)
                if poss_result is not None:
                    return poss_result

            if ip + int(program[ip][1]) == target_line:
                return acc
            ip += 1
            continue
        else:
            print('unrecognised instruction:', program[ip])

    return None

program = [line.strip().split() for line in sys.stdin.readlines()]
print(interpret(program, set(), 0, 0, True))
