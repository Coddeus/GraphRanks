from copy import deepcopy

# Generate all undirected graphs with n vertices -----------------------------------------------

def graphs(n):
    all_graphs = []
    edges = [str(i)+str(j) for i in range(n-1) for j in range(i+1, n)]

    for i in range(2**len(edges)):
        nb = str(bin(i)[2:])
        for i in range(len(edges)-len(nb)):
            nb = "0" + nb

        chosen = []
        for i in range(len(edges)):
            if nb[i]=='1':
                chosen.append(edges[i])
        all_graphs.append((list(map(str, range(n))), chosen))
    
    return all_graphs

# Generate the n-vertices complete graph -------------------------------------------------------

def complete(n):
    return (list(map(str, range(n))), [str(i)+str(j) for i in range(n-1) for j in range(i+1, n)])

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
    if any([i not in visited for i in in_reach]):
        visiting = []
        for v in in_reach:
            if v not in visited:
                visited.append(v)
                visiting.append(v)
        return any([findcycles(graph, basevertex, vertex, visited) for vertex in visiting])
    else:
        return False


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
    else:
        return "Not implemented yet!"

if __name__ == "__main__":
    # Directed graphs (vertices, edges), which edges direction will change.

    # Examples

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

    print()

    for g in graphs(4):
        print(n(0, g))
    
    print()

    for i in range(7):
        print(n(0, complete(i)))
