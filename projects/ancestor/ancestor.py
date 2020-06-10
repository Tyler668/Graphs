
from util import Stack, Queue
from graph import Graph


def get_parents(ancestors, child):
    parents = []

    for tup in ancestors:
        if tup[1] == child:
            parents.append(tup[0])
    return parents


ancestry = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
            (4, 8), (8, 9), (11, 8), (12, 1), (10, 2)]
kid = 6


def earliest_ancestor(ancestors, starting_node):
    visited = {}
    parents = get_parents(ancestors, starting_node)

    if len(parents) == 0:
        return -1

    s = Stack()
    s.push([starting_node])

    # path = []
    while s.size() > 0:
        path = s.pop()
        currentPerson = path[-1]

        if currentPerson not in visited:
            visited[currentPerson] = path

            parents = get_parents(ancestors, currentPerson)
            for parent in parents:
                pathCopy = list(path)
                pathCopy.append(parent)
                s.push(pathCopy)

    maxy = max(visited.values(), key=len)

    furthestRelatives = []
    for lst in visited.values():
        if len(lst) == len(maxy):
            for key, value in visited.items():
                if value == lst:
                    furthestRelatives.append(key)

    print('Maxy;', maxy)
    print('Furthest relatives determined to be: ', furthestRelatives)

    smallestFurthestRelative = min(furthestRelatives)

    # compare = [k = for key in visited.keys()]

    return smallestFurthestRelative

# ------------------------------------------------------------------------


print(earliest_ancestor(ancestry, 6))
