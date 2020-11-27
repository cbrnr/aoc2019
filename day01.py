def fuel(mass, recursive=False):
    """Compute fuel consumption of mass m.

    Parameters
    ----------
    mass : int
        Mass of a module.
    recursive : bool
        If False, use simple fuel calculation for part 1.
        If True, recursively compute fuel consumption for part 2.

    Returns
    -------
    f : int
        Fuel consumption.
    """
    f = mass // 3 - 2
    if not recursive:
        return f
    if f > 0:
        return f + fuel(f, recursive)
    return 0


# mass of all modules on the spacecraft (puzzle input)
masses = [112908, 61769, 65967, 51494, 99689, 114098, 135346, 59561, 147324,
          50465, 117491, 77845, 91959, 59847, 84013, 85763, 62121, 58965,
          89809, 97870, 77696, 70218, 118404, 83505, 141729, 61534, 101073,
          131358, 76104, 120836, 109789, 96510, 65406, 117906, 74921, 95412,
          99875, 134298, 105235, 82802, 103392, 81906, 133786, 140681, 109004,
          148434, 92333, 83848, 98297, 95728, 138202, 79312, 55633, 138461,
          50293, 141922, 140303, 66542, 50054, 99076, 143201, 66702, 133583,
          70308, 146824, 95606, 63054, 129272, 133051, 58626, 119896, 66265,
          99925, 131752, 74669, 148387, 132124, 107188, 55535, 145004, 78122,
          50885, 70325, 100859, 86484, 88795, 148164, 64473, 143089, 121023,
          52904, 120927, 87164, 133709, 89427, 105350, 106378, 98492, 78394,
          145200]

print("Part 1:", sum([fuel(m) for m in masses]))
print("Part 2:", sum([fuel(m, True) for m in masses]))
