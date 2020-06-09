
from util import Stack, Queue
from graph import Graph

def get_parents(ancestors, child):
    parents = []

    for tup in ancestors:
        if tup[1] == child:
            parents.append(tup[0])
    return parents
    # if len(parents) > 0:
    #     return parents
    # return None 

ancestry = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (12, 1), (10, 2) ]
kid = 6

# def earliest_ancestor(ancestors, starting_node):
#     g = Graph()
#     # g.add_vertex(starting_node)

    
#     for tup in ancestors:
#         if tup[1] not in g.vertices:
#             g.vertices[tup[1]] = set()
#             g.vertices[tup[1]].add(tup[0])
#         else:
#             g.vertices[tup[1]].add(tup[0])

#     print(g.vertices)
#     earliestAncestor = None
#     while g.get_neighbors(starting_node) != 0:
#         earliestAncestor = min(list(g.vertices[starting_node]))
#         starting_node = earliestAncestor
#     return earliestAncestor




            

#     print(g.vertices)




# print(get_parents(ancestors, child))

# def earliest_ancestor(ancestors, starting_node):
#     parents = get_parents(ancestors, starting_node)
#     if len(parents) == 0:
#         return -1

#     s = Stack()
#     s.push((starting_node))
    
#     paths = []

#     path = []
#     while s.size() > 0:
#         kid = s.pop()
#         path.append(kid)

        
#         parents = get_parents(ancestors, kid)
#         if len(parents) == 0:
#             paths.append(path)
#             path = [starting_node]

#         for parent in parents:    
#             s.push((parent))
#         # gen += 1
        
#     print(paths)
    # return visited[-1]

# def earliest_ancestor(ancestors, starting_node, gen = 0):
#     parents = get_parents(ancestors, starting_node)
#     if len(parents) == 0:
#         return -1

#     q = Queue()
#     q.enqueue((starting_node, 0))

#     visited = []

#     while q.size() > 0:
#         kid = q.dequeue()
#         visited.append(kid)

#         parents = get_parents(ancestors, kid[0])

#         for parent in parents:    
#             q.enqueue((parent, gen))
        
        
#     print(visited)
#     return visited[-1][0]



    # parents = get_parents(ancestors, starting_node)
    # generations.append(parents)

    # next_gen = []
    # for parent in parents:
    #     next_gen.append(get_parents(ancestors, parent))
    # generations.append(next_gen)

    # while len(parents) != 0:
    #     print('Parent', parents)
    #     for parent in parents:
    #         earliest_ancestor(ancestors, parent)
    # else:
    # return starting_node
    
    

    # print('HERE')
    # return starting_node




# print(len(get_parents(ancestry, 10)))
# (12, 2), (20, 4), (30, 11), (60, 30),(42, 10), (18, 2)

# ------------------------------------------------------------------------
# For test passage
# ------------------------------------------------------------------------
def earliest_ancestor(ancestors, starting_node):
    parents = get_parents(ancestors, starting_node)
    if len(parents) == 0:
        return -1

    s = Stack()
    s.push((starting_node))
    
    # paths = []

    path = []
    while s.size() > 0:
        kid = s.pop()
        path.append(kid)

        
        parents = get_parents(ancestors, kid)
        # if len(parents) == 0:
        #     paths.append(path)
        #     path = [starting_node]

        for parent in parents:    
            s.push((parent))
        # gen += 1
        
    # print(path)
    return path[-1]

# ------------------------------------------------------------------------

            
print(earliest_ancestor(ancestry, 6))