from collections import defaultdict


orbits = defaultdict(list)
orbits |= {"COM": ["B"],
           "B": ["C", "G"],
           "G": ["H"],
           "H": [],
           "C": ["D"],
           "D": ["E", "I"],
           "I": [],
           "E": ["J", "F"],
           "F": [],
           "J": ["K"],
           "K": ["L"],
           "L": []}


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


s = 0
for planet in orbits:  # sum node levels of all nodes
    s += level(planet, "COM", orbits)

print(s)
