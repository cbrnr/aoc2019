from day05 import run_intcode


with open("day09.txt") as f:
    file = f.read().strip()
intcode = tuple(int(i) for i in file.split(","))

program = run_intcode(intcode, 1)
for output in program:
    print("Part 1:", output)

program = run_intcode(intcode, 2)
for output in program:
    print("Part 2:", output)
