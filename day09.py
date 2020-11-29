with open("day09.txt") as f:
    file = f.read().strip()
intcode = tuple(int(i) for i in file.split(","))
