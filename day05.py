from enum import IntEnum
import logging


class OpCode(IntEnum):
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    JIT = 5
    JIF = 6
    LT = 7
    EQU = 8
    BASE = 9
    HALT = 99


class Mode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


def v(intcode, op, mode=Mode.POSITION, base=0):
    if mode == Mode.POSITION:
        return intcode[op]
    elif mode == Mode.IMMEDIATE:
        return op
    elif mode == Mode.RELATIVE:
        return intcode[base + op]


def run_intcode(intcode, inp, phase=None):
    """Run Intcode program.

    Parameters
    ----------
    intcode : list or tuple of int
        Intcode program as a list (or tuple) of integers.
    inp : int
        Input parameter.
    phase : int | None
        Phase setting.

    Yields
    ------
    output : int
        Output for each output instruction.
    """
    intcode = list(intcode)  # make a list copy
    ip = 0  # initialize instruction pointer
    base = 0  # initialize relative base
    while True:
        opcode = int(f"{intcode[ip]:05}"[-2:])
        m1, m2, m3 = (int(m) for m in f"{intcode[ip]:05}"[-3::-1])
        msg = f"{ip:5} | {opcode:2} {OpCode(opcode).name:6} | "
        if opcode == OpCode.ADD:
            op1, op2, op3 = intcode[ip + 1:ip + 4]
            v1, v2 = v(intcode, op1, m1, base), v(intcode, op2, m2, base)
            msg += f"{op1} ({v1}) + {op2} ({v2}) = {v1 + v2} → {op3}"
            intcode[op3] = v1 + v2
            ip += 4
        elif opcode == OpCode.MULT:
            op1, op2, op3 = intcode[ip + 1:ip + 4]
            v1, v2 = v(intcode, op1, m1, base), v(intcode, op2, m2, base)
            msg += f"{op1} ({v1}) * {op2} ({v2}) = {v1 * v2} → {op3}"
            intcode[op3] = v1 * v2
            ip += 4
        elif opcode == OpCode.INPUT:
            op1 = intcode[ip + 1]
            if phase is not None:  # if available, phase is the first input
                msg += f"{phase} → {op1}"
                intcode[op1] = phase
                phase = None
            else:
                msg += f"{inp} → {op1}"
                intcode[op1] = inp
            ip += 2
        elif opcode == OpCode.OUTPUT:
            op1 = intcode[ip + 1]
            output = v(intcode, op1, m1, base)
            msg += f"{op1} → {output}"
            ip += 2
            inp = yield output
        elif opcode == OpCode.JIT:
            op1, op2 = intcode[ip + 1:ip + 3]
            v1, v2 = v(intcode, op1, m1, base), v(intcode, op2, m2, base)
            msg += f"{op1} ({v1}) → {op2}"
            ip = v2 if v1 != 0 else ip + 3
        elif opcode == OpCode.JIF:
            op1, op2 = intcode[ip + 1:ip + 3]
            v1, v2 = v(intcode, op1, m1, base), v(intcode, op2, m2, base)
            msg += f"{op1} ({v1}) → {op2}"
            ip = v2 if v1 == 0 else ip + 3
        elif opcode == OpCode.LT:
            op1, op2, op3 = intcode[ip + 1:ip + 4]
            v1, v2 = v(intcode, op1, m1, base), v(intcode, op2, m2, base)
            msg += f"{op1} ({v1}) < {op2} ({v2}) → {op3}"
            intcode[op3] = 1 if v1 < v2 else 0
            ip += 4
        elif opcode == OpCode.EQU:
            op1, op2, op3 = intcode[ip + 1:ip + 4]
            v1, v2 = v(intcode, op1, m1, base), v(intcode, op2, m2, base)
            msg += f"{op1} ({v1}) == {op2} ({v2}) → {op3}"
            intcode[op3] = 1 if v1 == v2 else 0
            ip += 4
        elif opcode == OpCode.BASE:
            op1 = intcode[ip + 1]
            v1 = v(intcode, op1, m1, base)
            base += v1
        elif opcode == OpCode.HALT:  # halt
            break
        else:  # error
            raise ValueError(f"Unknown opcode {opcode}.")
        logging.info(msg)


intcode = (3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 101, 71, 150, 224,
           101, -123, 224, 224, 4, 224, 102, 8, 223, 223, 101, 2, 224, 224, 1,
           224, 223, 223, 2, 205, 209, 224, 1001, 224, -3403, 224, 4, 224,
           1002, 223, 8, 223, 101, 1, 224, 224, 1, 223, 224, 223, 1101, 55, 24,
           224, 1001, 224, -79, 224, 4, 224, 1002, 223, 8, 223, 101, 1, 224,
           224, 1, 223, 224, 223, 1, 153, 218, 224, 1001, 224, -109, 224, 4,
           224, 1002, 223, 8, 223, 101, 5, 224, 224, 1, 224, 223, 223, 1002,
           201, 72, 224, 1001, 224, -2088, 224, 4, 224, 102, 8, 223, 223, 101,
           3, 224, 224, 1, 223, 224, 223, 1102, 70, 29, 225, 102, 5, 214, 224,
           101, -250, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224,
           1, 223, 224, 223, 1101, 12, 52, 225, 1101, 60, 71, 225, 1001, 123,
           41, 224, 1001, 224, -111, 224, 4, 224, 102, 8, 223, 223, 1001, 224,
           2, 224, 1, 223, 224, 223, 1102, 78, 66, 224, 1001, 224, -5148, 224,
           4, 224, 1002, 223, 8, 223, 1001, 224, 2, 224, 1, 223, 224, 223,
           1101, 29, 77, 225, 1102, 41, 67, 225, 1102, 83, 32, 225, 1101, 93,
           50, 225, 1102, 53, 49, 225, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999,
           1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999,
           1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105,
           1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294,
           0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1,
           225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1107,
           677, 677, 224, 1002, 223, 2, 223, 1005, 224, 329, 101, 1, 223, 223,
           7, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 344, 1001, 223, 1,
           223, 7, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 359, 101, 1,
           223, 223, 1108, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 374,
           1001, 223, 1, 223, 8, 226, 677, 224, 1002, 223, 2, 223, 1006, 224,
           389, 1001, 223, 1, 223, 1108, 226, 677, 224, 1002, 223, 2, 223,
           1006, 224, 404, 101, 1, 223, 223, 1107, 677, 226, 224, 102, 2, 223,
           223, 1006, 224, 419, 101, 1, 223, 223, 1007, 677, 677, 224, 1002,
           223, 2, 223, 1005, 224, 434, 101, 1, 223, 223, 7, 677, 226, 224,
           102, 2, 223, 223, 1006, 224, 449, 1001, 223, 1, 223, 1008, 226, 677,
           224, 1002, 223, 2, 223, 1006, 224, 464, 101, 1, 223, 223, 8, 677,
           677, 224, 1002, 223, 2, 223, 1006, 224, 479, 101, 1, 223, 223, 108,
           226, 226, 224, 102, 2, 223, 223, 1005, 224, 494, 101, 1, 223, 223,
           1107, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 509, 101, 1, 223,
           223, 107, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 524, 1001,
           223, 1, 223, 107, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 539,
           101, 1, 223, 223, 1007, 226, 226, 224, 102, 2, 223, 223, 1006, 224,
           554, 101, 1, 223, 223, 108, 677, 677, 224, 102, 2, 223, 223, 1005,
           224, 569, 101, 1, 223, 223, 107, 677, 226, 224, 102, 2, 223, 223,
           1005, 224, 584, 101, 1, 223, 223, 1008, 226, 226, 224, 102, 2, 223,
           223, 1006, 224, 599, 101, 1, 223, 223, 1108, 677, 226, 224, 1002,
           223, 2, 223, 1006, 224, 614, 101, 1, 223, 223, 8, 677, 226, 224,
           102, 2, 223, 223, 1005, 224, 629, 1001, 223, 1, 223, 1008, 677, 677,
           224, 102, 2, 223, 223, 1006, 224, 644, 101, 1, 223, 223, 1007, 226,
           677, 224, 102, 2, 223, 223, 1005, 224, 659, 101, 1, 223, 223, 108,
           226, 677, 224, 102, 2, 223, 223, 1006, 224, 674, 101, 1, 223, 223,
           4, 223, 99, 226)

if __name__ == "__main__":
    for output in run_intcode(intcode, 1):
        pass
    print("Part 1:", output)
    assert output == 4511442

    for output in run_intcode(intcode, 5):
        pass
    print("Part 2:", output)
    assert output == 12648139
