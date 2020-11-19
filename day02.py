def run_intcode(intcode, noun, verb):
    """Run Intcode program.

    Parameters
    ----------
    intcode : list of int
        The Intcode program as a list of integers.
    noun : int
        Value which overwrites Intcode address 1.
    verb : int
        Value which overwrites Intcode address 2.

    Returns
    -------
    result : list of int
        The resulting Intcode after running the program.
    """
    intcode = list(intcode)  # make a list copy
    intcode[1], intcode[2] = noun, verb  # overwrite addresses 1 and 2
    ip = 0  # initialize instruction pointer
    while ip < len(intcode):
        try:  # get instruction
            opcode, *parameters = intcode[ip:ip + 4]
        except ValueError:  # less than 4 values available
            op1 = intcode[ip]  # this must be 99
        op1, op2, op3 = parameters
        if opcode == 1:
            intcode[op3] = intcode[op1] + intcode[op2]
        elif opcode == 2:
            intcode[op3] = intcode[op1] * intcode[op2]
        elif opcode == 99:
            break
        ip += 4
    return intcode


intcode = (1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 19,
           6, 23, 1, 23, 6, 27, 1, 13, 27, 31, 2, 13, 31, 35, 1, 5, 35, 39, 2,
           39, 13, 43, 1, 10, 43, 47, 2, 13, 47, 51, 1, 6, 51, 55, 2, 55, 13,
           59, 1, 59, 10, 63, 1, 63, 10, 67, 2, 10, 67, 71, 1, 6, 71, 75, 1,
           10, 75, 79, 1, 79, 9, 83, 2, 83, 6, 87, 2, 87, 9, 91, 1, 5, 91, 95,
           1, 6, 95, 99, 1, 99, 9, 103, 2, 10, 103, 107, 1, 107, 6, 111, 2, 9,
           111, 115, 1, 5, 115, 119, 1, 10, 119, 123, 1, 2, 123, 127, 1, 127,
           6, 0, 99, 2, 14, 0, 0)
print("Part 1:", run_intcode(intcode, 12, 2)[0])

output = 19690720  # desired output
for noun in range(100):
    for verb in range(100):
        if run_intcode(intcode, noun, verb)[0] == output:
            print("Part 2:", 100 * noun + verb)
            break
