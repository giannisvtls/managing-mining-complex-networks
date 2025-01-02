from itertools import combinations
import time

def triplets(graph):
    print('Running Triplets Algorithm...')
    start_time = time.time()
    triangles = 0
    nodes = list(graph.nodes())
    for u, v, w in combinations(nodes, 3):  #all triplets in our graph
        if graph.has_edge(u, v) and graph.has_edge(v, w) and graph.has_edge(w, u): # check if the edges between the three nodes exist
            triangles += 1
    print("--- %s seconds ---" % (time.time() - start_time))

    return triangles