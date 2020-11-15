def has_same_adjacent(n):
    """Determine if a number n has two adjacent digits that are the same.

    Parameters
    ----------
    n : int
        Number.

    Returns
    -------
    answer : bool
        Whether or not n has two adjacent digits that are the same.
    """
    n = str(n)
    i = 1
    while i < len(n):
        if n[i] == n[i - 1]:
            return True  # found two identical adjacent digits
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

print(counter)
