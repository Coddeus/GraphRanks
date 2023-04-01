from copy import deepcopy

# n(0, P) --------------------------------------------------------------------------------------

def reachable_vertices(graph, vertex):
    edges = []
    for e in graph[1]:
        if vertex == e[0]:
            edges.append(e[1])
    
    return edges


def findcycles(graph, basevertex, vertex, visited=[]):
    in_reach = reachable_vertices(graph, vertex)
    if basevertex in in_reach:
        return True
    if len(visited) == len(graph[0]):
        return False
    else:
        for v in in_reach:
            visited.append(v)
        return any([findcycles(graph, basevertex, vertex, visited) for vertex in in_reach])


def cyclic(graph, binary) -> bool:
    for n, bit in enumerate(binary):
        if bit=='1':
            graph[1][n] = ''.join(reversed(graph[1][n]))

    for v in graph[0]:
        if findcycles(graph, v, v, []):
            return True
    return False


def tryall(graph):
    globals()["in_reach"] = {vert: reachable_vertices(graph, vert) for vert in graph[0]}
    coc = 0 # Cyclic Orientations Count
    for i in range(2**len(graph[1])):
        nb = str(bin(i)[2:])
        for i in range(len(graph[1])-len(nb)):
            nb = "0" + nb

        if cyclic(deepcopy(graph), nb):
            coc+=1
    return coc

# ----------------------------------------------------------------------------------------------

def n(k, P):
    if k==0:
        return tryall(P)

if __name__ == "__main__":
    # Directed graphs (vertices, edges), which edges direction will change.

    G1 = (
        ["A", "B", "C", "D", "E"],
        ["AB", "BC", "CD", "DE", "EA", "BE"]
    )

    G2 = (
        ["A", "B", "C", "D"],
        ["AB", "BC", "CD", "DA", "AC"]
    )

    print(n(0, G1))
    print(n(0, G2))
