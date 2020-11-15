def has_same_adjacent(n, exact=False):
    """Determine if a number n has two adjacent digits that are the same.

    Parameters
    ----------
    n : int
        Number.
    exact : bool
        Whether or not there need to be exactly two digits. If False, there can
        also be more than two adjacent digits that are the same.

    Returns
    -------
    answer : bool
        Whether or not n has two adjacent digits that are the same.
    """
    n = str(n)
    i = 1
    # list that will contain zeros for digit pairs that are different and ones
    # for pairs that are the same; one zero is prepended and appended so that
    # when searching for exactly two adjacent digits that are the same, we only
    # need to search for [0, 1, 0] in this list
    same = [0]
    while i < len(n):
        if n[i] == n[i - 1]:
            if not exact:
                return True  # if there can be at least two digits we're done
            same.append(1)
        else:
            same.append(0)
        i += 1
    same.append(0)
    i = 2
    while i < len(same):
        if same[i - 2:i + 1] == [0, 1, 0]:  # this is a group of two digits
            return True
        i += 1
    return False


def increases_monotonically(n):
    """Determine if digits of a number n increase monotonically.

    Parameters
    ----------
    n : int
        Number.

    Returns
    -------
    answer : bool
        Whether or not digits of n increase monotonically.
    """
    n = str(n)
    i = 1
    while i < len(n):
        if n[i] < n[i - 1]:  # current digit is smaller than preceding digit
            return False
        i += 1
    return True


counter = 0
for n in range(130254, 678275 + 1):
    if has_same_adjacent(n) and increases_monotonically(n):
        counter += 1

print("Part 1:", counter)

counter = 0
for n in range(130254, 678275 + 1):
    if has_same_adjacent(n, exact=True) and increases_monotonically(n):
        counter += 1

print("Part 2:", counter)
