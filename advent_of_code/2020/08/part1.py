import sys

def interpret(program):
    acc = 0 # accumulator
    ip = 0 # instruction pointer
    seen = set() # seen line numbers
    while True:
        if ip in seen:
            return acc
        seen.add(ip)

        instruction = program[ip][0]
        if instruction == 'acc':
            acc += int(program[ip][1])
            ip += 1
            continue
        elif instruction == 'jmp':
            ip += int(program[ip][1])
            continue
        elif instruction == 'nop':
            ip += 1
            continue
        else:
            print('unrecognised instruction:', program[ip])

    return -1

program = [line.strip().split() for line in sys.stdin.readlines()]
print(interpret(program))
