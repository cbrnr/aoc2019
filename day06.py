from collections import defaultdict


def create_orbits(s):
    """Create an orbit map (tree) from a string description.

    Parameters
    ----------
    s : str
        Orbit map defined in a string containing one item per line formatted as
        XXX)YYY (YYY orbits XXX).

    Returns
    -------
    orbits : dict
        Orbit map as a tree. Each node (key) contains its children (value).
    """
    orbits = defaultdict(list)
    for orbit in s.split():
        key, value = orbit.split(")")
        orbits[key].append(value)
        orbits[value]  # make sure every child is created
    return orbits


def level(node, root, tree):
    """Return level of a given node in a tree.

    Parameters
    ----------
    node : str
        Node in a tree.
    root : str
        Root node (by definition this is level 0).
    tree : dict
        A tree stored in a dictionary. The keys are the nodes, and the values
        are lists of children nodes.

    Returns
    -------
    lvl : int
        The node level in the tree.
    """
    for key, value in tree.items():
        if node in value:
            if key == root:  # root
                return 1
            else:
                return 1 + level(key, root, tree)
    else:
        if node == root:
            return 0  # node was root
        else:
            raise KeyError(f"Node '{node}' not found.")


description = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
orbits = create_orbits(description)
s = 0
for planet in orbits:  # sum node levels of all nodes
    s += level(planet, "COM", orbits)

print(s)
